---
UID : NC:d3d10umddi.PFND3D11DDI_RECYCLECREATEDEFERREDCONTEXT
title : PFND3D11DDI_RECYCLECREATEDEFERREDCONTEXT
author : windows-driver-content
description : The RecycleCreateDeferredContext function clears out the pipeline state for a deferred context.
old-location : display\recyclecreatedeferredcontext.htm
old-project : display
ms.assetid : c9e08048-683a-4f43-b3b8-1914c2933a5c
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : RecycleCreateDeferredContext is supported beginning with the Windows 7 operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RecycleCreateDeferredContext
req.alt-loc : d3d10umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11DDI_RECYCLECREATEDEFERREDCONTEXT callback function
The <i>RecycleCreateDeferredContext</i> function clears out the pipeline state for a deferred context.

## Syntax

```
PFND3D11DDI_RECYCLECREATEDEFERREDCONTEXT Pfnd3d11ddiRecyclecreatedeferredcontext;

HRESULT Pfnd3d11ddiRecyclecreatedeferredcontext(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATEDEFERREDCONTEXT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

<i>RecycleCreateDeferredContext</i> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The deferred context is successfully created.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><i>RecycleCreateDeferredContext</i> could not allocate memory that is required for it to complete.

## Remarks

The driver is only required to implement <i>RecycleCreateDeferredContext</i> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 threading-capability bit. The driver can return D3D11DDICAPS_COMMANDLISTS_BUILD_2 in the <b>Caps</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_threading_caps.md">D3D11DDI_THREADING_CAPS</a> structure from a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10_2ddi_getcaps.md">GetCaps(D3D10_2)</a> function.

For more information about <i>RecycleCreateDeferredContext</i>, see <a href="https://msdn.microsoft.com/a417bcc7-ca86-4853-baa3-415214da348f">Introduction to Deferred Contexts</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_threading_caps.md">D3D11DDI_THREADING_CAPS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_createdeferredcontext.md">D3D11DDIARG_CREATEDEFERREDCONTEXT</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10_2ddi_getcaps.md">GetCaps(D3D10_2)</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_RECYCLECREATEDEFERREDCONTEXT callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>