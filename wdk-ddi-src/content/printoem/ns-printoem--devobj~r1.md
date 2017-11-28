---
UID: NS.printoem._DEVOBJ~r1
title: DEVOBJ
author: windows-driver-content
description: The DEVOBJ structure is used as an input argument to several of a rendering plug-in's COM interface methods.
old-location: print\devobj.htm
old-project: print
ms.assetid: cdcd0437-e4fc-4041-827f-caa3c435325c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DEVOBJ, DEVOBJ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVOBJ
req.alt-loc: printoem.h
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
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# DEVOBJ structure



## -description
<p>The DEVOBJ structure is used as an input argument to several of a rendering plug-in's COM interface methods.</p>


## -syntax

````
typedef struct _DEVOBJ {
  DWORD     dwSize;
  PDEVOEM   pdevOEM;
  HANDLE    hEngine;
  HANDLE    hPrinter;
  HANDLE    hOEM;
  PDEVMODE  pPublicDM;
  PVOID     pOEMDM;
  PDRVPROCS pDrvProcs;
} DEVOBJ;
````


## -struct-fields
<dl>

### -field <b>dwSize</b>

<dd>
<p>Specifies the size, in bytes, of the DEVOBJ structure. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field <b>pdevOEM</b>

<dd>
<p>Pointer to the rendering plug-in's private PDEV structure, as returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554249">IPrintOemUni::EnablePDEV</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553215">IPrintOemPS::EnablePDEV</a>. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field <b>hEngine</b>

<dd>
<p>GDI handle to the physical device. This handle is received by the printer driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556181">DrvCompletePDEV</a> function, as the function's <i>hdev</i> argument.</p>
</dd>

### -field <b>hPrinter</b>

<dd>
<p>Spooler's handle to the printer. This handle is received by the printer driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a> function, as the function's <i>hDriver</i> argument.</p>
</dd>

### -field <b>hOEM</b>

<dd>
<p>Plug-in instance handle. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field <b>pPublicDM</b>

<dd>
<p>Pointer to the printer's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field <b>pOEMDM</b>

<dd>
<p>Pointer to the rendering plug-in's private DEVMODEW structure members. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field <b>pDrvProcs</b>

<dd>
<p>
      Not used. In a previous version of the interface, this was a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548571">DRVPROCS</a> structure.</p>
</dd>
</dl>

## -remarks
<p>The DEVOBJ structure is accessible to graphics DDI hooking functions through the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569901">SURFOBJ</a> structure's <b>dhpdev</b> member. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554249">IPrintOemUni::EnablePDEV</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553215">IPrintOemPS::EnablePDEV</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554249">IPrintOemUni::EnablePDEV</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553215">IPrintOemPS::EnablePDEV</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556181">DrvCompletePDEV</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569901">SURFOBJ</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20DEVOBJ structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
