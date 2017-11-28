---
UID: NS.bdamedia._KSM_BDA_PIN
title: KSM_BDA_PIN
author: windows-driver-content
description: The KSM_BDA_PIN structure describes a method request to create or delete a pin factory for a filter.
old-location: stream\ksm_bda_pin.htm
old-project: stream
ms.assetid: 7e7778ba-cf4f-44e8-91ce-c53458d3db9a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KSM_BDA_PIN, KSM_BDA_PIN, *PKSM_BDA_PIN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdamedia.h
req.include-header: Bdamedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSM_BDA_PIN
req.alt-loc: bdamedia.h
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

# KSM_BDA_PIN structure



## -description
<p>The KSM_BDA_PIN structure describes a method request to create or delete a pin factory for a filter. </p>


## -syntax

````
typedef struct _KSM_BDA_PIN {
  KSMETHOD Method;
  union {
    ULONG PinId;
    ULONG PinType;
  };
  ULONG    Reserved;
} KSM_BDA_PIN, *PKSM_BDA_PIN;
````


## -struct-fields
<dl>

### -field <b>Method</b>

<dd>
<p>KSMETHOD structure that describes a method and request type of a method request.</p>
</dd>

### -field <b>PinId</b>

<dd>
<p>Member of the union in KSM_BDA_PIN that contains the identifier (ID) of a pin factory of a filter.</p>
</dd>

### -field <b>PinType</b>

<dd>
<p>Member of the union in KSM_BDA_PIN that contains the value that specifies the pin type.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
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
<dt>Bdamedia.h (include Bdamedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSM_BDA_PIN structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
