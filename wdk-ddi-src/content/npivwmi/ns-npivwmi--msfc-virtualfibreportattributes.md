---
UID: NS.npivwmi._MSFC_VirtualFibrePortAttributes
title: MSFC_VirtualFibrePortAttributes
author: windows-driver-content
description: The MSFC_VirtualFibrePortAttributes structure contains attribute information for a virtual port.
old-location: storage\msfc_virtualfibreportattributes.htm
old-project: storage
ms.assetid: FD8D6063-E6DD-4EA6-9675-774C58C08B40
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MSFC_VirtualFibrePortAttributes, MSFC_VirtualFibrePortAttributes, *PMSFC_VirtualFibrePortAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: npivwmi.h
req.include-header: Npivwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSFC_VirtualFibrePortAttributes
req.alt-loc: npivwmi.h
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
req.iface: 
---

# MSFC_VirtualFibrePortAttributes structure



## -description
<p>The MSFC_VirtualFibrePortAttributes structure contains attribute information for a virtual port.</p>


## -syntax

````
typedef struct _MSFC_VirtualFibrePortAttributes {
  ULONG  Status;
  ULONG  FCId;
  USHORT VirtualName[64];
  UCHAR  Tag[16];
  UCHAR  WWPN[8];
  UCHAR  WWNN[8];
  UCHAR  FabricWWN[8];
} MSFC_VirtualFibrePortAttributes, *PMSFC_VirtualFibrePortAttributes;
````


## -struct-fields
<dl>

### -field Status

<dd>
<p>The virtual port status.</p>
</dd>

### -field FCId

<dd>
<p>The fabric ID of the virtual port.</p>
</dd>

### -field VirtualName

<dd>
<p>The symbolic name of the virtual port.</p>
</dd>

### -field Tag

<dd>
<p>A value for identifying the virtual port. This member provides a 128-bit width to accommodate a unique identifier.</p>
</dd>

### -field WWPN

<dd>
<p>The world wide port name of the physical port.</p>
</dd>

### -field WWNN

<dd>
<p>The world wide node name of the physical port.</p>
</dd>

### -field FabricWWN

<dd>
<p>The world wide port name of the fabric.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Npivwmi.h (include Npivwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.msfc_virtualfibreportattributes_wmi_class">MSFC_VirtualFibrePortAttributes WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSFC_VirtualFibrePortAttributes structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
