---
UID: NF.prcomoem.IPrintOemUni.DriverDMS
title: IPrintOemUni::DriverDMS method
author: windows-driver-content
description: The IPrintOemUni::DriverDMS method allows a rendering plug-in for Unidrv to indicate that it uses a device-managed drawing surface.
old-location: print\iprintoemuni_driverdms.htm
old-project: print
ms.assetid: b62e6752-0804-41c4-84f4-49ad145acaf3
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IPrintOemUni, IPrintOemUni::DriverDMS, DriverDMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUni.DriverDMS
req.alt-loc: prcomoem.h
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
req.product: Windows 10 or later.
---

# IPrintOemUni::DriverDMS method



## -description
The <code>IPrintOemUni::DriverDMS</code> method allows a rendering plug-in for <a href="wdkgloss.u#wdkgloss.unidrv#wdkgloss.unidrv"><i>Unidrv</i></a> to indicate that it uses a device-managed drawing surface.



## -syntax

````
HRESULT DriverDMS(
   PVOID  pDevObj,
   PVOID  pBuffer,
   DWORD  cbSize,
   PDWORD pcbNeeded
);
````


## -parameters

### -param pDevObj 

Caller-supplied pointer to a <a href="print.devobj">DEVOBJ</a> structure.


### -param pBuffer 

Caller-supplied pointer to a buffer to receive method-specified flags. (See the following Remarks section.)


### -param cbSize 

Caller-supplied size, in bytes, of the buffer pointed to by <i>pBuffer</i>.


### -param pcbNeeded 

Caller-supplied pointer to a location to receive the required minimum <i>pBuffer</i> size.


## -returns
The method must return one of the following values.
<dl>
<dt><b>S_OK</b></dt>
</dl>The operation succeeded.
<dl>
<dt><b>E_FAIL</b></dt>
</dl>The operation failed

 


## -remarks
A rendering plug-in for Unidrv must implement the <code>IPrintOemUni::DriverDMS</code> method. The method will be called only if Unidrv finds a valid interface pointer to the OEM's rendering plug-in.

The <code>IPrintOemUni::DriverDMS</code> method allows a rendering plug-in to indicate that it will be using a device-managed drawing surface instead of the default GDI-managed surface.

The method must specify HOOK_-prefixed flags in the buffer pointed to by <i>pBuffer</i>, indicating which of the plug-in's graphics DDI hooking functions are to be called for the drawing surface. The HOOK_-prefixed flags are defined in winddi.h and described in the <a href="display.engassociatesurface">EngAssociateSurface</a> function's description. Flags specified by <code>IPrintOemUni::DriverDMS</code> are passed by Unidrv to <b>EngAssociateSurface</b>. (Note that to support a device-managed surface, the rendering plug-in must hook out all drawing functions.) For more information, see <a href="https://msdn.microsoft.com/4403165f-c528-450e-9c96-77a9ce0778aa">Handling Device-Managed Surfaces</a>.

If <code>IPrintOemUni::DriverDMS</code> sets flags in the buffer pointed to by <i>pBuffer</i>, Unidrv creates a device-managed surface by calling <a href="display.engcreatedevicesurface">EngCreateDeviceSurface</a>. If <code>IPrintOemUni::DriverDMS</code> does not set any flags, Unidrv creates a GDI-managed surface by calling <a href="display.engcreatebitmap">EngCreateBitmap</a>. In either of these cases, <code>IPrintOemUni::DriverDMS</code> should return S_OK.

If the output buffer size specified by <i>cbSize</i> is too small, the method should specify the required size in the location pointed to by <i>pcbNeeded</i>, call <b>SetLastError</b>(ERROR_INSUFFICIENT_BUFFER), and return E_FAIL.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>