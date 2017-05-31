# wagtail-apps

Apps based around content types that can be implemented in a Wagtail site using Bootstrap markup.

Many apps will have an app-nameIndex and an app-namePage. The app_nameIndex is a parent that will autopopulate with app_namePage

**about** - an AboutPage that displays "about" information in one long page, naviagble via scrollspy.

**blog** - simple BlogIndex and BlogPage.

**casestudies** - CaseStudiesIndex displays content via clickable "cards" with an image and title. Clicking will take you through to the CaseStudy.

**documents** - DocumentPage that creates an archive of documents. Uses scrollspy to display section headings and documents names on the side 
for easy navigation

**events** - most fully featured app. Includes two pages, an EventIndex (parent) and EventPage (child) 
The EventPage has social as well as add to calendar buttons. EventIndex is autopopulated with content from the EventPage including
the aforementioned buttons with a click through for mor einformation. 

**FAQ** - Simple FAQ page created using Question and Answer blocks. Is displayed via collapsable panels.

**ourresearch** - works similar to the casestudies app except instead of using images on the card is uses FontAwesome icons. Currently
has three layers a OurResearchIndex (with all the different disciplines), that leads to a OurResearchSubject (which acts as an index page
for the subjects), to the OurResearchArticle (which populates the OurResearchSUbject).

**technical** - a more advanced "AboutPage" that can create sub-headings in the scrollspy menu.

