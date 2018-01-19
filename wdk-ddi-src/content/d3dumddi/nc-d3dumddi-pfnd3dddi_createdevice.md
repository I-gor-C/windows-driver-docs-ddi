---
UID : NC:d3dumddi.PFND3DDDI_CREATEDEVICE
title : PFND3DDDI_CREATEDEVICE
author : windows-driver-content
description : The CreateDevice function creates a graphics context that is referenced in subsequent calls.
old-location : display\createdevice.htm
old-project : display
ms.assetid : ce35bdac-af90-471f-af93-0e665be6c7f6
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_PTE, DXGK_PTE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : CreateDevice
req.alt-loc : d3dumddi.h
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
req.typenames : DXGK_PTE
---


# PFND3DDDI_CREATEDEVICE callback function
The <b>CreateDevice</b> function creates a graphics context that is referenced in subsequent calls.

## Syntax

```
PFND3DDDI_CREATEDEVICE Pfnd3dddiCreatedevice;

HRESULT Pfnd3dddiCreatedevice(
  HANDLE hAdapter,
  D3DDDIARG_CREATEDEVICE *
)
{...}
```

## Parameters

`hAdapter`

A handle that identifies the graphics adapter.

`*`




## Return Value

<b>CreateDevice</b> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The graphics context is successfully created.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createdevice.md">CreateDevice</a> could not allocate the memory that was required for it to complete.

## Remarks

A display device is a graphics context that is used to hold a collection of rendering state. Multiple devices can be created by the same process on a given adapter. Note that the number of display devices that can simultaneously exist is limited only by available system memory. That is, a driver cannot hardcode a maximum device limit.

Generally, devices are independent of each other, so that resources that are created in one device cannot be referenced or accessed by resources that are created in another. However, cross-process resources are an exception to this rule.

When the Direct3D runtime calls <b>CreateDevice</b> to create a device, the runtime does not create a default graphics processing unit (GPU) context thread of execution for the device. The driver must explicitly call the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function to create one or more contexts as required.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_adapterfuncs.md">D3DDDI_ADAPTERFUNCS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_createdevice.md">D3DDDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_destroydevice.md">DestroyDevice</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CREATEDEVICE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>