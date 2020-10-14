describe('App', () => {
  beforeEach(() => {
    cy.visit('/', () => {

    })
  })

  it('Should have populated select', () => {
    const countrySelectOptions = cy.get("#country_select option")
    countrySelectOptions.should('have.length', 251)
  })

  it('should show selected country on select change', () => {
    cy.get('#country_select').select('France')
    cy.get('#selected_country > h2').contains('France')
  })

  it('should add country to favourties on button click', () => {
    cy.get('#country_select').select('France')
    cy.get('button').click()
    cy.get('li').contains('France')
  })
})
