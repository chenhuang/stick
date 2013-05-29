// Copyright 2006-2007 javascript-array.com

var timeout	= 500;
var closetimer	= 0;
var ddmenuitem	= 0;

// open hidden layer
function mopen(id)
{	
	// cancel close timer
	mcancelclosetime();

	// close old layer
	if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';

	// get new layer and show it
	ddmenuitem = document.getElementById(id);
	ddmenuitem.style.visibility = 'visible';

}
// close showed layer
function mclose()
{
	if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
}

// go close timer
function mclosetime()
{
	closetimer = window.setTimeout(mclose, timeout);
}

// cancel close timer
function mcancelclosetime()
{
	if(closetimer)
	{
		window.clearTimeout(closetimer);
		closetimer = null;
	}
}

function draw_frame() {
    body = $("#wrap");
    body.prepend(
'<table><tr><td><img src="http://stick.ischool.umd.edu/BugOnLeave.png" alt="" width="92" height="72" /></td><td></td><td><p align=justify><font face="Verdana" size="6" color="#006699"> <strong>S</strong></font><strong><font face="Verdana" size="6" color="#006699">TICK</font><br /><font face="Verdana" size="3" color="#006699"> Science &amp; Technology Innovation Concept Knowledge-base</font>      </b></strong></td>    </tr>     </table> <ul id="sddm">	<li><a href="http://stick.ischool.umd.edu/index.htm">Home</a></li>     <li><a href="http://stick.ischool.umd.edu/news.htm">News and Events</a></li>     <li><a href="http://stick.ischool.umd.edu/project.htm"onmouseover="mopen(\'m2\')"          onmouseout="mclosetime()">About Us</a>       <div id="m2"             onmouseover="mcancelclosetime()"            onmouseout="mclosetime()"> 	<a href="http://stick.ischool.umd.edu/project.htm">Project Description &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a> 	<a href="http://stick.ischool.umd.edu/people.htm">Project Team</a>         </div>     </li>     <li><a href="http://stick.ischool.umd.edu/publications.htm">Publications</a></li><li><a href="http://stick.ischool.umd.edu/details.html"onmouseover="mopen(\'m1\')"onmouseout="mclosetime()">Details</a><div id="m1"onmouseover="mcancelclosetime()"onmouseout="mclosetime()"><a href="http://stick.ischool.umd.edu/innovation_ecosystem.html">Innovation Eco-System</a><a href="http://stick.ischool.umd.edu/stick_framework.html">STICK Framework</a><a href="http://stick.ischool.umd.edu/building_innovation_knowledgebase.html">Building the Innovation Knowledge-base</a><a href="http://stick.ischool.umd.edu/data_collection_processing.html">Data Collection and Processing</a><a href="http://stick.ischool.umd.edu/innovation_ontology.html">Innovation Ontology</a><a href="http://stick.ischool.umd.edu/case_studies.html">Case/Pilot Studies</a><a href="http://stick.ischool.umd.edu/data_analysis_and_visualization.html">Data Analysis and Visualization</a></div></li><li><a href="http://stick.ischool.umd.edu/contact.htm">Contact</a></li> </ul> <div style="clear:both"></div>');
    body.append(
'<div id="footer"><table WIDTH="800" style="border-left-width: 0; border-right-width: 0; border-top-width: 0; border-bottom-style: solid; border-bottom-width: 0" id="AutoNumber1" > <tr> <td><img border="0" src="http://stick.ischool.umd.edu/nsf%20logo.jpg" align="justify" width="35" height="32"></td> <td>This project is supported by the National Science Foundation, </span> <span style="FONT-STYLE: italic; FONT-FAMILY: Verdana">Award Number </span> </font><i><span class="pageheadsubline"><strong style="font-weight: 400"> <font size="2" face="Verdana" color="#006699"> <a href="http://www.nsf.gov/awardsearch/showAward.do?AwardNumber=0915645" target="_blank" style="text-decoration: none"> <font color="#006699">0915645</font></a></font></strong></span></i><font size="2" color="#666666"><span style="FONT-STYLE: italic; FONT-FAMILY: Verdana"> </span><span style="font-family: Verdana; font-style:italic"> under the </span> </font><span style="font-family: Verdana; font-style:italic"> <a href="http://www.nsf.gov/funding/pgm_summ.jsp?pims_id=501084" target="_blank" style="text-decoration: none"> <font size="2" color="#006699">Science of Science and Innovation Policy</font></a><a href="http://www.nsf.gov/funding/pgm_summ.jsp?pims_id=11678&org=NSF" style="text-decoration: none"><font size="2" color="#666666">  program</font></a><font size="2" color="#666666">.</font></span> </td> </tr> </table> </div> '
);
}

function draw_bottom_banner() {

}

// close layer when click-out
document.onclick = mclose; 


