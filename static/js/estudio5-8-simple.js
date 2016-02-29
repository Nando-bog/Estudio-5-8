function hideshow(div_to_hide)
  {
    if (!document.getElementById)
      return
    if (div_to_hide.style.width=="50%")
    {
      //div_to_hide.style.display="none"
      div_to_hide.style.width="8em"
      div_to_hide.style.height="8em"
    }
    else
    //div_to_hide.style.display="block"
    div_to_hide.style.width="50%"
    div_to_hide.style.width="15em"
    
  }
