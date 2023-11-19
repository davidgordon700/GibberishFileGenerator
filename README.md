# GibberishFileGenerator
*Problem*: many projects need sample data or sample files.

*Solution*: Genearte gibberish files for testing and dev without using private or personal identifiable data.

References:
Text parts sourced from [byteshift.de?  lorem-ipsum generator](https://generator.lorem-ipsum.info/_latin)

cgn_canada_csv_eng.csv sourced from [Canadian Geographic Names](https://open.canada.ca/data/en/dataset/e27c6eba-3c5d-4051-9db2-082dc6411c2c)

Credit cards sourced from [Moneris](https://developer.moneris.com/More/Testing/Testing%20a%20Solution)

Images from [Stable Diffusion](https://stablediffusionweb.com/#ai-image-generator)

# Document types

Documents follow a naming convention to help users interpret what type of sample document is being viewed.

`"{doc type indicator}{year}-{month}.{sequence}B{batchName}.docx"`
doc type indicator - a letter or abbreviation indicator.  For example, documents starting with "C" are intended to be contracts.
year-month - an date part that can be used for filters and sorting.
sequence - an iteration counter to help make each file name unique.
batchName - a batch name to maintain unique file names across iterations.

## Contracts

doc type indicator = "C"

Contract types are defined in `ContractServices.txt` and initially include Web Design, Database Design, Painting, Snow removal, and Landscaping.

Document body includes:

>Document heading of `"Contract {year}-{month}.{sequence}"`
>
>First paragraph reads `"This is a contract between us and {company} for {random text}.`
>
>A short list of items and prices.
>
>A block of random concluding text.

## Application

doc type indicator = "A"

Application types are defined in `ApplicationTypes.txt` and initially include Housing, Learning Grant, Employment, Daycare Supplement, Rental, Assistance, Driver's Licence, Developer Licence, ABC Association, Membership, XYZ Association Membership, Construction Permit, and Dog Licence.

Document body includes:
>Document heading of `"Application: {applicationType}"`
>
>A "Application Details" sub heading
>
>Applicant details table including First Name, Last Name, and Date of Birth
>
>If the applicationType is in "Employment","Daycare Supplement", or "Driver's Licence" an image of the applicant is included.
>
>If the applicationType is "Dog Licence" an image of the dog is included.
>
>If the appicationType is not "Housing","Learning Grant","Employment","Daycare Supplement",
or "Rental Assistance" a credit card section is added including card number, CVC, and expiry date.
>
>All other applications include a "conditions" sub heading.

## Application Approval Letter

doc type indicator = "LApproval"

Document body includes:
>Salutation and client address
> 
>Regarding statement  `"Re: Approval {applicationType} application"`
>
>A "Application Details" sub heading
>
>Random blocks of text
>
>A "Sincerely" statement from a random clerk.

## Application Rejection Letter

doc type indicator = "LRejection"

Document body includes:
>Salutation and client address
> 
>Regarding statement  `"Re: Rejection {applicationType} application"`
>
>A "Application Details" sub heading
>
>Random blocks of text
>
>A "Sincerely" statement from a random supervisor.

## Reports

doc type indicator = "rpt"

A report is generated for each application type. 
Each report includes two worksheets - "data" and "Plot".

The data sheet has a row for the year 2000 to present with a random application count.

The Plot sheet has a bar chart of application count per year.
