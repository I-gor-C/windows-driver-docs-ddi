---
UID: NS.printoem._UNIDRV_PRIVATE_DEVMODE
title: UNIDRV_PRIVATE_DEVMODE
author: windows-driver-content
description: The UNIDRV_PRIVATE_DEVMODE structure enables Unidrv plug-ins to determine the size of the private portion of Unidrv's DEVMODEW structure.
old-location: print\unidrv_private_devmode.htm
old-project: print
ms.assetid: 91b8ba63-5276-43f8-81a6-07afc1a77ced
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: UNIDRV_PRIVATE_DEVMODE, UNIDRV_PRIVATE_DEVMODE, *PUNIDRV_PRIVATE_DEVMODE
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
req.alt-api: UNIDRV_PRIVATE_DEVMODE
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

# UNIDRV_PRIVATE_DEVMODE structure



## -description
<p>The UNIDRV_PRIVATE_DEVMODE structure enables Unidrv plug-ins to determine the size of the private portion of Unidrv's DEVMODEW structure.</p>


## -syntax

````
typedef struct _UNIDRV_PRIVATE_DEVMODE {
  WORD wReserved[4];
  WORD wSize;
} UNIDRV_PRIVATE_DEVMODE, *PUNIDRV_PRIVATE_DEVMODE;
````


## -struct-fields
<dl>

### -field wReserved

<dd>
<p>Reserved for system use.</p>
</dd>

### -field wSize

<dd>
<p>The size, in bytes, of the private portion of Unidrv's <a href="display.devmodew">DEVMODEW</a> structure.</p>
</dd>
</dl>

## -remarks
<p>This structure and associated macro are available in Windows 2000 and later. For information about the public and private sections of the DEVMODEW structure, see <a href="https://msdn.microsoft.com/26212e3b-a591-4ed6-b441-b130d8d4d948">The DEVMODEW Structure</a>.</p>

<p>Printoem.h defines a macro for determining the size of the private portion of Unidrv's DEVMODEW structure.</p>

<p>The pdm argument in the <b>GET_UNIDRV_PRIVATE_DEVMODE_SIZE</b> macro is a pointer to a DEVMODEW structure. The macro determines whether the value of the <b>dmDriverExtra</b> member of the DEVMODEW structure is larger than the byte offset of the <b>wSize</b> member of the UNIDRV_PRIVATE_DEVMODE structure. If so, the macro returns the value of the <b>wSize</b> member in the UNIDRV_PRIVATE_DEVMODE structure. If not, the macro returns zero.</p>

<p>To safely determine the address of the private portion of your plug-in's DEVMODEW structure, do the following:</p>

<p>Call the <b>GET_UNIDRV_PRIVATE_DEVMODE_SIZE</b> macro, passing the address of the DEVMODEW structure in the call.</p>

<p>Verify that (pdm)-&gt;dmDriverExtra is larger than the value returned by the macro. (The macro returns the value of the <b>wSize</b> member of the UNIDRV_PRIVATE_DEVMODE structure.)</p>

<p>The preceding example starts with the address of the public DEVMODEW structure (pdm), adds the number of bytes of this structure (pdm-&gt;dmSize), and then adds the size in bytes of the Unidrv private DEVMODEW structure (<b>wSize</b>). A plug-in's private DEVMODEW data begins at this memory address. If there are multiple plug-ins chained together, the address returned by this example is that of the first plug-in's private DEVMODEW data. The second plug-in's private DEVMODEW data follows the first plug-in's private DEVMODEW data, the third plug-in's private DEVMODEW data follows that of the second plug-in's private DEVMODEW data, and so on. A plug-in developer who needs to determine the address of the <i>n</i>-th plug-in's private DEVMODEW data must know the sizes of the private DEVMODEW data for the first <i>n</i> - 1 plug-ins.</p>

<p>Verify that the private portion of your plug-in's DEVMODEW structure begins with a valid <a href="..\printoem\ns-printoem--oem-dmextraheader.md">OEM_DMEXTRAHEADER</a> structure.</p>

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
<a href="..\printoem\ns-printoem--pscript5-private-devmode.md">PSCRIPT5_PRIVATE_DEVMODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20UNIDRV_PRIVATE_DEVMODE structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
