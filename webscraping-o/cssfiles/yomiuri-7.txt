.slick-slider {
  display: block!important;
}
.photo-slider {
  width: 600px; /* デフォルトの横幅 */
  display: none;
  margin: 0 auto;
  visibility: hidden;
}
.photo-slider .photo-slider-item {
  border: 5px solid transparent;
  box-sizing: border-box;
}
.photo-slider .photo-slider-item .photo-slider-item__thumb {
  align-items: center;
  background-color: #000;
  display: flex;
  /*justify-content: center;*/
  height: 120px;
}
.photo-slider .photo-slider-item .photo-slider-item__thumb img {
  height: auto;
  width: auto;
  max-height: 100%;
  max-width: 100%;
  margin: 0 auto;
}
/* IEハック用 */  
@media all and (-ms-high-contrast: none){
  .photo-slider .photo-slider-item .photo-slider-item__thumb img {
    width: 100%;
  }
}
.photo-slider .photo-slider-item a {
  color: #fff;
  text-decoration: none;
}
.photo-slider .photo-slider-item a figure {
  margin: 0;
}
.photo-slider .photo-slider-item figcaption {
  color: #1e2428;
  font-size: 14px;
  font-size: .875rem;
  padding-top: 5px;
}
.photo-slider .photo-slider-item a:hover figcaption{
  text-decoration: underline;
}

.photo-slider .photo-slider-item a:visited figcaption{
  color: #6b808e;
}
.photo-slider .photo-slider-item .photo-slider-item__date {
  color: #b4b4b4;
  font-size: 11px;
  font-size: .6875rem;
}
/* js生成部分 */
.photo-slider .slick-arrow {
  width: 32px;
  height: 50px;
  background-color: #616568;
  border: none;
  border-radius: 3px;
  color: transparent;
  font-size: 0;
  font-weight: 100;
  line-height: 1;
  cursor: pointer;
  padding: 0 7px;
}
.photo-slider .slick-arrow::before {
  box-sizing: border-box;
  display: block;
  height: 26px;
  padding: 0 3px;
}
.photo-slider .slick-arrow  .slick-arrow::before {
  border-top: 1px solid #fff;
  border-right: 1px solid #fff;
  content: "";
  display: block;
  height: 16px;
  opacity: 1;
  width: 16px;
}
.photo-slider .slick-prev {
  left: -60px;
}
.photo-slider .slick-prev .slick-prev::before {
  margin-left: 6px;
  transform: rotate(-135deg);
}
.photo-slider .slick-next {
  right: -60px;
}
.photo-slider .slick-next .slick-next::before {
  margin-left: -4px;
  transform: rotate(45deg);
}
.photo-slider .slick-prev:hover, .photo-slider .slick-prev:focus, .photo-slider .slick-next:hover, .photo-slider .slick-next:focus {
  background: #616568;
}
@media screen and (max-width: 599px) {
  .photo-slider {
      width: 100%;
  }
}