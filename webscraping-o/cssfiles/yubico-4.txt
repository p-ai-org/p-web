#cookie-law-info-bar,.wt-cli-cookie-bar{
	box-sizing: border-box;
	font-size: 10pt;
	margin: 0 auto;
	padding: 10px 10px;
	position: absolute;
	text-align: center;
	width: 100%;
	z-index: 99999;
	box-shadow:rgba(0,0,0,.5) 0px 5px 10px;
	display: none;
	left: 0px;
}
#cookie-law-info-again {
	font-size: 10pt;
	margin: 0;
	padding:5px 10px;
	text-align: center;
	z-index: 9999;
	cursor: pointer;
	box-shadow: #161616 2px 2px 5px 2px;
}
#cookie-law-info-bar span {
	vertical-align: middle;
}

/** Buttons (http://papermashup.com/demos/css-buttons) */
.cli-plugin-button, .cli-plugin-button:visited {
	display: inline-block;
	padding: 8px 16px 8px;
	color: #fff;
	text-decoration: none;
	-moz-border-radius: 4px;
	-webkit-border-radius: 4px;
	position: relative;
	cursor: pointer;
	text-decoration: none;
}
.cli-accept-button{ font-family: Courier; font-variant: small-caps;}

.cli-plugin-main-link {
	
}
.cli-plugin-button:hover {
	background-color: #111;
	color: #fff;
	text-decoration: none;
}
.small.cli-plugin-button, .small.cli-plugin-button:visited {
	font-size: 11px;
}
.cli-plugin-button, .cli-plugin-button:visited,
	.medium.cli-plugin-button, .medium.cli-plugin-button:visited {
	font-size: 13px;
	font-weight: 500;
	line-height: 1;
}
.large.cli-plugin-button, .large.cli-plugin-button:visited {
	font-size: 14px;
	padding: 8px 14px 9px;
}
.super.cli-plugin-button, .super.cli-plugin-button:visited {
	font-size: 34px;
	padding: 8px 14px 9px;
}
.pink.cli-plugin-button, .magenta.cli-plugin-button:visited {
	background-color: #e22092;
}
.pink.cli-plugin-button:hover {
	background-color: #c81e82;
}
.green.cli-plugin-button, .green.cli-plugin-button:visited {
	background-color: #91bd09;
}
.green.cli-plugin-button:hover {
	background-color: #749a02;
}
.red.cli-plugin-button, .red.cli-plugin-button:visited {
	background-color: #e62727;
}
.red.cli-plugin-button:hover {
	background-color: #cf2525;
}
.orange.cli-plugin-button, .orange.cli-plugin-button:visited {
	background-color: #ff5c00;
}
.orange.cli-plugin-button:hover {
	background-color: #d45500;
}
.blue.cli-plugin-button, .blue.cli-plugin-button:visited {
	background-color: #2981e4;
}
.blue.cli-plugin-button:hover {
	background-color: #2575cf;
}
.yellow.cli-plugin-button, .yellow.cli-plugin-button:visited {
	background-color: #ffb515;
}
.yellow.cli-plugin-button:hover {
	background-color: #fc9200;
}
.cli-bar-popup{
	-moz-background-clip: padding;
	-webkit-background-clip: padding;
	background-clip: padding-box;
	-webkit-border-radius:30px;
	-moz-border-radius:30px;
	border-radius:30px;
	padding:20px;
}
.cli-clearboth{
	clear:both;
}
@media only screen and (max-width:768px) {
    .cli-settings-mobile:hover {
        box-shadow:none !important;
    }
    .cli-settings-desktop {
        display: none;
    }
    .cli-col-8
    {
    	max-width:100% !important;
    	width:100% !important;
    	flex: 100% !important;
    	-ms-flex: 100% !important;
    }
    .cli-accordion-plusminus{
    	float: right; 
    	font-size:22px;
    	line-height: 22px;
    }
    .cli-plugin-button{
        margin:10px;
    }
}
@media only screen and (max-width:567px)
{
	.cli-switch .cli-slider:after
	{
		display: none;
	}
	.cli-tab-header a.cli-nav-link
	{
		font-size:12px;
	}
	.cli-modal .cli-modal-close
	{
		right:-10px;
		top:-15px;
	}
}

.wt-cli-iframe-placeholder {
    background-image: url(../images/cli_placeholder.svg);
	background-size: 80px;
	max-width:100%;
	max-height:100%;
    background-position: center;
    background-repeat: no-repeat;
    background-color: #b2b0b059;
    position: relative;
    display: flex;
	align-items: flex-end;
    justify-content: center;
}
.wt-cli-iframe-placeholder .wt-cli-inner-text {
    width: 100%;
    text-align: center;
    padding: 1rem 1rem;
    border-radius: 400px;
}
.wt-cli-cookie-bar-container
{
	display: none;
}
.wt-cli-necessary-checkbox {
    display: none !important;
}
a.wt-cli-ccpa-opt-out {
	text-decoration:underline !important;;
}