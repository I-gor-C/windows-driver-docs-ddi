---
UID: NS.ks.PKSPIN_PHYSICALCONNECTION
title: PKSPIN_PHYSICALCONNECTION
author: windows-driver-content
description: A structure of type KSPIN_PHYSICALCONNECTION is returned in response to a KSPROPERTY_PIN_PHYSICALCONNECTION request.
old-location: stream\kspin_physicalconnection.htm
old-project: stream
ms.assetid: e11c6e8d-a338-4427-af04-bdb07b9e9a73
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPIN_PHYSICALCONNECTION, KSPIN_PHYSICALCONNECTION, *PKSPIN_PHYSICALCONNECTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPIN_PHYSICALCONNECTION
req.alt-loc: ks.h
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

# PKSPIN_PHYSICALCONNECTION structure



## -description
<p>A structure of type KSPIN_PHYSICALCONNECTION is returned in response to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565205">KSPROPERTY_PIN_PHYSICALCONNECTION</a> request.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Pin;
  WCHAR SymbolicLinkName[1];
} KSPIN_PHYSICALCONNECTION, *PKSPIN_PHYSICALCONNECTION;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Specifies the size of the structure. Note that the structure contains a dynamic array.</p>
</dd>

### -field Pin

<dd>
<p>Specifies the PinId of the connected pin on the other filter. (Pin 2 of Wave is connected to Pin 1 of Topology.)</p>
</dd>

### -field SymbolicLinkName

<dd>
<p>Specifies a string containing the symbolic link name of the connected filter </p>
</dd>
</dl>

## -remarks
<p>This structure is used with port class only.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565205">KSPROPERTY_PIN_PHYSICALCONNECTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPIN_PHYSICALCONNECTION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
