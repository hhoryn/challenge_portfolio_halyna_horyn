# Task 1. Software Configuration
## Subtask 1. Why did I choose to participate in the portfolio challenge?
Hey! Nice to e-meet you :blush: 

I'm Halyna. A couple of weeks ago I came across an Insta ad saying "free QA Automated Testing course". So I thought: “Why not give it try?”. This happened literally 3 hours after I decided I needed to find a new direction, so it was probably **a sign**.

What I came to understand after working for an IT company is:

- I’ve always been intrigued by how computers work and the amazing things you can make them do;
- I don’t want to be stuck in Customer Support, I want to move forward in life and give ‘real’ IT a go. 

So that’s why I’m writing this message now. I really hope I’ll manage to complete this course and get plenty of new knowledge and a certificate.


Many thanks!

# Task 2. Selectors

Hi! I analized the 7 elements found on the [login page](https://scouts-test.futbolkolektyw.pl/en) and here are the xpath selectors I managed to construct:  
### Element 1. Scouts panel heading
- `//h5[contains(@class,'MuiTypography')]`;
- `//*[contains(text(),'Scouts Panel')]`;
- `//h5[contains(text(),'Scouts Panel')]`;
- `//h5[normalize-space(text())='Scouts Panel']`;
- `//div[contains(@class,'MuiCardContent-root')]//child::h5`.

### Element 2. Login field
- `//input[@id='login']`;
- `//input[@name='login']`;
- `//input[@type='text'] `.

### Element 3. Password field
- `//input[@id='password']`;
- `//input[@name='password']`;
- `//input[@type='password']`.

### Element 4. Language box (English)
- `//div[@role='button']`;
- `//div[text()='English']`;
- `//div[contains(text(),'English')]`;
- `//input[@aria-hidden='true']//preceding::div[1]`;
- `//input[@aria-hidden='true']//preceding-sibling::div`.

### Element 5. Language box (Polish)
- `//div[text()='Polski']`;
- `//div[@aria-haspopup='listbox']`;
- `//input[@value='pl']//preceding::div[1]`;
- `//input[@value='pl']//preceding-sibling::div`.

### Element 6. Remind password
- `//a[text()='Remind password']`;
- `//a[contains(text(),'Remind')]`;
- `//a[contains(text(),'Remind password')]`;
- `//a[@tabindex='-1']`.

### Element 7. Sign in
- `//button[@type='submit']`;
- `//button[@tabindex='0']`;
- `//span[text()='Sign in']//parent::button`;
- `//div[@class='MuiCardActions-root']//child::button`.



