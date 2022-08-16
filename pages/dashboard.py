from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_heading_xpath = "//h6[text()='Scouts Panel']"
    main_page_xpath = "//span[text()='Main page']"
    scouts_panel_logo_xpath = "//div[@title='Logo Scouts Panel']"
    add_player_button_xpath = "//span[text()='Add player']//parent::button"
    dev_team_contact_xpath = "//span[text()='Dev team contact']//parent::a"
    sign_out_heading_xpath = "span[text()='Sign out']"
    players_count_box_xpath = "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][1]"
    shortcuts_box_xpath = "//h2[text()='Shortcuts']//parent::div"
    toolbar_xpath = "//button[@aria-label='menu']//parent::div"
    payers_heading_xpath = "//span[text()='Players']"
