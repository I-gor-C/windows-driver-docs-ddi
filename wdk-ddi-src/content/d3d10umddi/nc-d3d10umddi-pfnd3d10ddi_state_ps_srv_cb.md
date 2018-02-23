---
UID: NC:d3d10umddi.PFND3D10DDI_STATE_PS_SRV_CB
title: PFND3D10DDI_STATE_PS_SRV_CB
author: windows-driver-content
description: The pfnStatePsSrvCb function causes the Microsoft Direct3D 10 runtime to refresh the pixel shader stage's bound shader resource views.
old-location: display\pfnstatepssrvcb.htm
old-project: display
ms.assetid: ed49ce47-c56d-4d38-8f2c-562841b8e804
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: display.pfnstatepssrvcb, pfnStatePsSrvCb callback function [Display Devices], pfnStatePsSrvCb, PFND3D10DDI_STATE_PS_SRV_CB, PFND3D10DDI_STATE_PS_SRV_CB, d3d10umddi/pfnStatePsSrvCb, d3d10state_functions_39451a84-f247-4325-bcc0-b9ee23c2cfe3.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	UserDefined
apilocation:
-	d3d10umddi.h
apiname:
-	pfnStatePsSrvCb
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10DDI_STATE_PS_SRV_CB callback function
The <b>pfnStatePsSrvCb</b> function causes the Microsoft Direct3D 10 runtime to refresh the pixel shader stage's bound shader resource views.

## Syntax

```
PFND3D10DDI_STATE_PS_SRV_CB Pfnd3d10ddiStatePsSrvCb;

void Pfnd3d10ddiStatePsSrvCb(
   D3D10DDI_HRTCORELAYER,
   UINT,
   UINT
)
{...}
```

## Parameters

`D3D10DDI_HRTCORELAYER`



`UINT`



`UINT`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_createdevice.md">CreateDevice(D3D10)</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_corelayer_devicecallbacks.md">D3D10DDI_CORELAYER_DEVICECALLBACKS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_STATE_PS_SRV_CB callback function%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>