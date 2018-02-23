---
UID: NS:d3dumddi._D3DDDI_BLTFLAGS
title: "_D3DDDI_BLTFLAGS"
author: windows-driver-content
description: The D3DDDI_BLTFLAGS structure identifies the type of bit-block transfer (bitblt) to perform.
old-location: display\d3dddi_bltflags.htm
old-project: display
ms.assetid: 844d6aed-2ca2-45ef-bd53-54344dbdadbf
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: d3dumddi/D3DDDI_BLTFLAGS, display.d3dddi_bltflags, _D3DDDI_BLTFLAGS, D3DDDI_BLTFLAGS structure [Display Devices], D3D_other_Structs_8d70fa64-3813-4165-a64d-4e91287e05d5.xml, D3DDDI_BLTFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dumddi.h
apiname:
-	D3DDDI_BLTFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_BLTFLAGS
---

# _D3DDDI_BLTFLAGS structure
The D3DDDI_BLTFLAGS structure identifies the type of bit-block transfer (bitblt) to perform.

## Syntax
````
typedef struct _D3DDDI_BLTFLAGS {
  union {
    struct {
      UINT Point  :1;
      UINT Linear  :1;
      UINT SrcColorKey  :1;
      UINT DstColorKey  :1;
      UINT MirrorLeftRight  :1;
      UINT MirrorUpDown  :1;
      UINT LinearToSrgb  :1;
      UINT Rotate  :1;
      UINT BeginPresentToDwm  :1;
      UINT ContinuePresentToDwm  :1;
      UINT EndPresentToDwm  :1;
#if (D3D_UMD_INTERFACE_VERSION < D3D_UMD_INTERFACE_VERSION_WIN8)
      UINT Reserved  :21;
#else 
      UINT Discard  :1;
      UINT NoOverwrite  :1;
      UINT Tileable  :1;
      UINT Reserved  :18;
#endif 
    };
    UINT Value;
  };
} D3DDDI_BLTFLAGS;
````

## Members


## Remarks
The <b>BeginPresentToDwm</b>, <b>ContinuePresentToDwm</b>, and <b>EndPresentToDwm</b> bit-field flags inform the user-mode display driver about the time when the Direct3D runtime performs parts of a DWM present operation.  Because DWM present operations can occur in multiple steps, the Direct3D runtime uses these flags to mark the steps in a sequence of bitblts. For example:  

<ul>
<li>If the present operation consists of one bitblt, the bitblt is marked as follows:<ul>
<li><b>BeginPresentToDwm</b> = <b>TRUE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>TRUE</b>;</li>
</ul>
</li>
<li>If the present operation consists of two bitblts, the bitblts are marked as shown in two sequential bitblt operations:<ol>
<li>First bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>TRUE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>FALSE</b>;</li>
</ul>
</li>
<li>Second bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>TRUE</b>;</li>
</ul>
</li>
</ol>
</li>
<li>If the present operation consists of three or more bitblts, the bitblts are marked as shown in the following sequential bitblt operations:<ol>
<li>First bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>TRUE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>FALSE</b>;</li>
</ul>
</li>
<li>Second and successive bitblts, not including the final bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>TRUE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>FALSE</b>;</li>
</ul>
</li>
<li>Final bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>TRUE</b>;</li>
</ul>
</li>
</ol>
</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_flush.md">Flush</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_blt.md">D3DDDIARG_BLT</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_BLTFLAGS structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>