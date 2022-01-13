import json
from geopy.geocoders import Nominatim

coordinate_output = {}
loc = Nominatim(user_agent="GetLoc")
allschools = ['A. Mario Loiederman Middle Sch', 'Albert Einstein High School', 'Alternative Ed', 'Arcola Elementary School', 'Argyle Middle School', 'Ashburton Elementary School', 'Bannockburn Elementary School', 'Bayard Rustin Elementary Schl', 'Beall Elementary School', 'Bel Pre Elementary School', 'Bells Mill Elementary School', 'Belmont Elementary School', 'Benjamin Banneker Middle Schl', 'Bethesda Elementary School', 'Bethesda-Chevy Chase High Schl', 'Beverly Farms Elementary Schl', 'Bradley Hills Elementary Schl', 'Briggs Chaney Middle School', 'Brooke Grove Elementary School', 'Brookhaven Elementary School', 'Brown Station Elementary Schl', 'Burning Tree Elementary School', 'Burnt Mills Elementary School', 'Burtonsville Elementary School', 'Cabin John Middle School', 'Candlewood Elementary School', 'Cannon Road Elementary School', 'Capt. James Daly Elementary', 'Carderock Springs Elem School', 'Carl Sandburg Learning Center', 'Cashell Elementary School', 'Cedar Grove Elementary School', 'Chevy Chase Elementary School', 'Clarksburg Elementary School', 'Clarksburg High School', 'Clearspring Elementary School', 'Clopper Mill Elementary School', 'Cloverly Elementary School', 'Col. Zadok Magruder High Schl', 'Cold Spring Elementary School', 'College Gardens Elem School', 'Cresthaven Elementary School', 'Damascus Elementary School', 'Damascus High School', 'Darnestown Elementary School', 'Diamond Elementary School', 'Dr. Charles Drew Elem School', 'Dr. Martin Luther King, Jr. MS', 'Dr. Sally K. Ride Elem School', 'DuFief Elementary School', 'Earle B. Wood Middle School', 'East Silver Spring Elem School', 'Eastern Middle School', 'Fairland Elementary School', 'Fallsmead Elementary School', 'Farmland Elementary School', 'Fields Road Elementary School', 'Flora M. Singer Elem School', 'Flower Hill Elementary School', 'Flower Valley Elem School', 'Forest Knolls Elem School', 'Forest Oak Middle School', 'Fox Chapel Elementary School', 'Francis Scott Key Middle Schl', 'Gaithersburg Elementary School', 'Gaithersburg High School', 'Gaithersburg Middle School', 'Galway Elementary School', 'Garrett Park Elementary School', 'Georgian Forest Elem School', 'Germantown Elementary School', 'Glen Haven Elementary School', 'Glenallan Elementary School', 'Goshen Elementary School', 'Great Seneca Creek Elem School', 'Greencastle Elementary School', 'Greenwood Elementary School', 'Hallie Wells Middle Sch', 'Harmony Hills Elem School', 'Herbert Hoover Middle School', 'Highland Elementary School', 'Highland View Elem School', 'Jackson Road Elem School', 'James Hubert Blake High School', 'JoAnn Leleck ES at Broad Acres', 'John F. Kennedy High School', 'John Poole Middle School', 'John T. Baker Middle School', 'Jones Lane Elementary School', 'Judith A. Resnik Elem School', 'Julius West Middle School', 'Kemp Mill Elementary School', 'Kensington-Parkwood Elem Schl', 'Kingsview Middle School', 'Lake Seneca Elementary School', 'Lakelands Park Middle School', 'Lakewood Elementary School', 'Laytonsville Elementary School', 'Little Bennett Elementary Schl', 'Lois P. Rockwell Elementary', 'Longview School', 'Lucy V. Barnsley Elementary', 'Luxmanor Elementary School', 'Maryvale Elementary School', 'Meadow Hall Elementary School', 'Mill Creek Towne Elem School', 'Monocacy Elementary School', 'Montgomery Blair High School', 'Montgomery Knolls Elem School', 'Montgomery Village Middle Schl', 'Neelsville Middle School', 'New Hampshire Estates ES', 'Newport Mill Middle School', 'North Bethesda Middle School', 'North Chevy Chase Elem School', 'Northwest High School', 'Northwood High School', 'Oak View Elementary School', 'Oakland Terrace Elem School', 'Odessa Shannon Middle Schl', 'Olney Elementary School', 'Paint Branch High School', 'Parkland Middle School', 'Pine Crest Elementary School', 'Piney Branch Elementary School', 'Poolesville Elementary School', 'Poolesville High School', 'Potomac Elementary School', 'Quince Orchard High School', 'Rachel Carson Elem School', 'Redland Middle School', 'RICA - Reg Inst for Child/Adol', 'Richard Montgomery High School', 'Ridgeview Middle School', 'Ritchie Park Elementary School', 'Robert Frost Middle School', 'Roberto Clemente Middle School', 'Rock Creek Forest Elementary', 'Rock Creek Valley Elem School', 'Rock Terrace School', 'Rock View Elementary School', 'Rockville High School', 'Rocky Hill Middle School', 'Rolling Terrace Elem School', 'Ronald McNair Elem', 'Rosa M. Parks Middle School', 'Roscoe R. Nix Elementary', 'Rosemary Hills Elem School', 'Rosemont Elementary School', 'S. Christa McAuliffe ES', 'Sargent Shriver Elem School', 'Seneca Valley High School', 'Sequoyah Elementary School', 'Seven Locks Elementary School', 'Shady Grove Middle School', 'Sherwood Elementary School', 'Sherwood High School', 'Silver Creek Middle School', 'Silver Spring International MS', 'Sligo Creek Elementary School', 'Sligo Middle School', 'Snowden Farm ES', 'Somerset Elementary School', 'South Lake Elementary School', 'Spark M. Matsunaga Elem School', 'Springbrook High School', 'Stedwick Elementary School', 'Stephen Knolls School', 'Stone Mill Elementary School', 'Stonegate Elementary School', 'Strathmore Elementary School', 'Strawberry Knoll Elem School', 'Summit Hall Elementary School', 'Takoma Park Elementary School', 'Takoma Park Middle School', 'Thomas S. Wootton High School', 'Thomas W. Pyle Middle School', 'Thurgood Marshall Elem School', 'Tilden Middle School', 'Travilah Elementary School', 'Twinbrook Elementary School', 'Viers Mill Elementary School', 'Walt Whitman High School', 'Walter Johnson High School', 'Washington Grove Elem School', 'Waters Landing Elementary Schl', 'Watkins Mill Elementary School', 'Watkins Mill High School', 'Wayside Elementary School', 'Weller Road Elementary School', 'Westbrook Elementary School', 'Westland Middle School', 'Westover Elementary School', 'Wheaton High School', 'Wheaton Woods Elementary Schl', 'Whetstone Elementary School', 'White Oak Middle School', 'William B. Gibbs, Jr. ES', 'William H. Farquhar Middle Sch', 'William Tyler Page ES', 'Wilson Wims Elementary School', 'Winston Churchill High School', 'Wood Acres Elementary School', 'Woodfield Elementary School', 'Woodlin Elementary School', 'Wyngate Elementary School']
firsthalfschools = ['A. Mario Loiederman Middle School', 'Albert Einstein High School', 'Alternative Ed', 'Arcola Elementary School', 'Argyle Middle School', 'Ashburton Elementary School', 'Bannockburn Elementary School', 'Bayard Rustin Elementary School', 'Beall Elementary School', 'Bel Pre Elementary School', 'Bells Mill Elementary School', 'Belmont Elementary School', 'Benjamin Banneker Middle School', 'Bethesda Elementary School', 'Bethesda-Chevy Chase High School', 'Beverly Farms Elementary School', 'Bradley Hills Elementary School', 'Briggs Chaney Middle School', 'Brooke Grove Elementary School', 'Brookhaven Elementary School', 'Brown Station Elementary School', 'Burning Tree Elementary School', 'Burnt Mills Elementary School', 'Burtonsville Elementary School', 'Cabin John Middle School', 'Candlewood Elementary School', 'Cannon Road Elementary School', 'Capt. James Daly Elementary School', 'Carderock Springs Elementary School', 'Carl Sandburg Learning Center', 'Cashell Elementary School', 'Cedar Grove Elementary School', 'Chevy Chase Elementary School', 'Clarksburg Elementary School', 'Clarksburg High School', 'Clearspring Elementary School', 'Clopper Mill Elementary School', 'Cloverly Elementary School', 'Col. Zadok Magruder High School', 'Cold Spring Elementary School', 'College Gardens Elementary School', 'Cresthaven Elementary School', 'Damascus Elementary School', 'Damascus High School', 'Darnestown Elementary School', 'Diamond Elementary School', 'Dr. Charles Drew Elementary School', 'Dr. Martin Luther King, Jr. MS', 'Dr. Sally K. Ride Elementary School', 'DuFief Elementary School', 'Earle B. Wood Middle School', 'East Silver Spring Elementary School', 'Eastern Middle School', 'Fairland Elementary School', 'Fallsmead Elementary School', 'Farmland Elementary School', 'Fields Road Elementary School', 'Flora M. Singer Elementary School', 'Flower Hill Elementary School', 'Flower Valley Elementary School', 'Forest Knolls Elementary School', 'Forest Oak Middle School', 'Fox Chapel Elementary School', 'Francis Scott Key Middle School', 'Gaithersburg Elementary School', 'Gaithersburg High School', 'Gaithersburg Middle School', 'Galway Elementary School', 'Garrett Park Elementary School', 'Georgian Forest Elementary School', 'Germantown Elementary School', 'Glen Haven Elementary School', 'Glenallan Elementary School', 'Goshen Elementary School', 'Great Seneca Creek Elementary School', 'Greencastle Elementary School', 'Greenwood Elementary School', 'Hallie Wells Middle School', 'Harmony Hills Elementary School', 'Herbert Hoover Middle School', 'Highland Elementary School', 'Highland View Elementary School', 'Jackson Road Elementary School', 'James Hubert Blake High School', 'JoAnn Leleck ES at Broad Acres', 'John F. Kennedy High School', 'John Poole Middle School', 'John T. Baker Middle School', 'Jones Lane Elementary School', 'Judith A. Resnik Elementary School', 'Julius West Middle School', 'Kemp Mill Elementary School', 'Kensington-Parkwood Elementary School', 'Kingsview Middle School', 'Lake Seneca Elementary School', 'Lakelands Park Middle School', 'Lakewood Elementary School', 'Laytonsville Elementary School', 'Little Bennett Elementary School', 'Lois P. Rockwell Elementary School', 'Longview School', 'Lucy V. Barnsley Elementary School', 'Luxmanor Elementary School', 'Maryvale Elementary School', 'Meadow Hall Elementary School']
schools = ['Mill Creek Towne Elementary School', 'Monocacy Elementary School', 'Montgomery Blair High School', 'Montgomery Knolls Elementary School', 'Montgomery Village Middle School', 'Neelsville Middle School', 'New Hampshire Estates ES', 'Newport Mill Middle School', 'North Bethesda Middle School', 'North Chevy Chase Elementary School', 'Northwest High School', 'Northwood High School', 'Oak View Elementary School', 'Oakland Terrace Elementary School', 'Odessa Shannon Middle School', 'Olney Elementary School', 'Paint Branch High School', 'Parkland Middle School', 'Pine Crest Elementary School', 'Piney Branch Elementary School', 'Poolesville Elementary School', 'Poolesville High School', 'Potomac Elementary School', 'Quince Orchard High School', 'Rachel Carson Elementary School', 'Redland Middle School', 'RICA - Reg Inst for Child/Adol', 'Richard Montgomery High School', 'Ridgeview Middle School', 'Ritchie Park Elementary School', 'Robert Frost Middle School', 'Roberto Clemente Middle School', 'Rock Creek Forest Elementary School', 'Rock Creek Valley Elementary School', 'Rock Terrace School', 'Rock View Elementary School', 'Rockville High School', 'Rocky Hill Middle School', 'Rolling Terrace Elementary School', 'Ronald McNair Elem', 'Rosa M. Parks Middle School', 'Roscoe R. Nix Elementary School', 'Rosemary Hills Elementary School', 'Rosemont Elementary School', 'S. Christa McAuliffe ES', 'Sargent Shriver Elementary School', 'Seneca Valley High School', 'Sequoyah Elementary School', 'Seven Locks Elementary School', 'Shady Grove Middle School', 'Sherwood Elementary School', 'Sherwood High School', 'Silver Creek Middle School', 'Silver Spring International MS', 'Sligo Creek Elementary School', 'Sligo Middle School', 'Snowden Farm ES', 'Somerset Elementary School', 'South Lake Elementary School', 'Spark M. Matsunaga Elementary School', 'Springbrook High School', 'Stedwick Elementary School', 'Stephen Knolls School', 'Stone Mill Elementary School', 'Stonegate Elementary School', 'Strathmore Elementary School', 'Strawberry Knoll Elementary School', 'Summit Hall Elementary School', 'Takoma Park Elementary School', 'Takoma Park Middle School', 'Thomas S. Wootton High School', 'Thomas W. Pyle Middle School', 'Thurgood Marshall Elementary School', 'Tilden Middle School', 'Travilah Elementary School', 'Twinbrook Elementary School', 'Viers Mill Elementary School', 'Walt Whitman High School', 'Walter Johnson High School', 'Washington Grove Elementary School', 'Waters Landing Elementary School', 'Watkins Mill Elementary School', 'Watkins Mill High School', 'Wayside Elementary School', 'Weller Road Elementary School', 'Westbrook Elementary School', 'Westland Middle School', 'Westover Elementary School', 'Wheaton High School', 'Wheaton Woods Elementary School', 'Whetstone Elementary School', 'White Oak Middle School', 'William B. Gibbs, Jr. ES', 'William H. Farquhar Middle School', 'William Tyler Page ES', 'Wilson Wims Elementary School', 'Winston Churchill High School', 'Wood Acres Elementary School', 'Woodfield Elementary School', 'Woodlin Elementary School', 'Wyngate Elementary School']
for school in range(len(schools)):
    try:
        getLoc = loc.geocode(f"{schools[school]}, Montgomery County")
        coordinate_output[allschools[len(firsthalfschools) + school]] = {"latitude": getLoc.latitude, "longitude": getLoc.longitude}
    except AttributeError:
        coordinate_output[allschools[len(firsthalfschools) + school]] = {"latitude": 0, "longitude": 0}
        print(f"{schools[school]} has no coords")
        continue

with open('coordinates.json', "w") as outputfile:
    outputfile.write(json.dumps(coordinate_output, indent=4))

#geopy rate limits all schools so you have to run the program twice and save first coordinatejson locally

#additionally, some schools don't have coordinates (we have to manually input them)
# some places aren't even schools so they're omitted from the coordinate json file