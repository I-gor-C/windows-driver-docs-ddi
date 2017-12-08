---
UID: NS.ks.PKSPROPERTY_SERIAL
title: PKSPROPERTY_SERIAL
author: windows-driver-content
description: The KSPROPERTY_SERIAL structure is a header that is included for each property that follows a KSPROPERTY_SERIALHDR structure.
old-location: stream\ksproperty_serial.htm
old-project: stream
ms.assetid: 751bf70d-0602-487a-82c7-efca075b8968
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_SERIAL, KSPROPERTY_SERIAL, *PKSPROPERTY_SERIAL
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
req.alt-api: KSPROPERTY_SERIAL
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

# PKSPROPERTY_SERIAL structure



## -description
<p>The KSPROPERTY_SERIAL structure is a header that is included for each property that follows a KSPROPERTY_SERIALHDR structure.</p>


## -syntax

````
typedef struct {
  KSIDENTIFIER PropTypeSet;
  ULONG        Id;
  ULONG        PropertyLength;
} KSPROPERTY_SERIAL, *PKSPROPERTY_SERIAL;
````


## -struct-fields
<dl>

### -field PropTypeSet

<dd>
<p>A structure of type <a href="stream.ksidentifier">KSIDENTIFIER</a> that specifies the type of property data. This is the same information obtained from querying Basic Support.</p>
</dd>

### -field Id

<dd>
<p>Specifies the identifier for this property.</p>
</dd>

### -field PropertyLength

<dd>
<p>Specifies the length, in bytes, of the following property data. This does not include any alignment buffering that may be appended to the property data before the next property in the serialization.</p>
</dd>
</dl>

## -remarks
<p>A KSPROPERTY_SERIAL structure is followed by the property data, with the start of each property on FILE_LONG_ALIGNMENT. Note that the serial header structure itself is also defined to be on FILE_LONG_ALIGNMENT.</p>

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
<a href="stream.ksproperty_serialhdr">KSPROPERTY_SERIALHDR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_SERIAL structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
