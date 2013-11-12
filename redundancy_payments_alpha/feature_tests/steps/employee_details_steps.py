from insolvency_practitioner_forms import routes

ip_test_client = routes.app.test_client()

@given('an IP entering the employee details')
def step(context):
    context.form_data = {}
    for row in context.table:
        context.form_data[row['DETAILS']] = row['VALUE']

@when('the IP goes to {url}')
def step(context, url):
    form = ip_test_client.get(url)
    context.form_data['csrf_token'] = parse_csrf_token(form)

@when('enters the employee details')
def step(context):
    context.response_from_posting_data = ip_test_client.post(
        '/create-employee-record/employee-details/',
        data=context.form_data
    )

@then('the IP should be sent to {url}')
def step(context, url):
    assert_that(context.response_from_posting_data.status, is_('302 FOUND'))
    headers = context.response_from_posting_data.headers
    redirect_path = headers['Location']
    assert_that(redirect_path, contains_string(url))


@then("the data base should contain an employee")
def step(context):
    session = make_session()
    try:
        employee = session.query(Employee).all() [0]
        assert_that(employee.nino, is_(context.form_data["employee_national_insurance_number"]))
    finally:
        session.close()