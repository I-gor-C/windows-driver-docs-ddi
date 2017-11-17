---
UID: NS.ksmedia.PKSEVENT_TUNER_INITIATE_SCAN_S
title: PKSEVENT_TUNER_INITIATE_SCAN_S
author: windows-driver-content
description: The KSEVENT_TUNER_INITIATE_SCAN_S structure is used in the KSEVENT_TUNER_INITIATE_SCAN event within the EVENTSETID_TUNER event set.
old-location: stream\ksevent_tuner_initiate_scan_s.htm
ms.assetid: e690c596-d339-4489-97f3-02cacfdc5b04
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSEVENT_TUNER_INITIATE_SCAN_S
req.alt-loc: ksmedia.h
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
ms.keywords: PKSEVENT_TUNER_INITIATE_SCAN_S, KSEVENT_TUNER_INITIATE_SCAN_S, *PKSEVENT_TUNER_INITIATE_SCAN_S
req.iface: 
---

# PKSEVENT_TUNER_INITIATE_SCAN_S structure



## -description
<p>The KSEVENT_TUNER_INITIATE_SCAN_S structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561898">KSEVENT_TUNER_INITIATE_SCAN</a> event within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559566">EVENTSETID_TUNER</a> event set. </p>


## -syntax

````
typedef struct {
  KSEVENTDATA EventData;
  ULONG       StartFrequency;
  ULONG       EndFrequency;
} KSEVENT_TUNER_INITIATE_SCAN_S, *PKSEVENT_TUNER_INITIATE_SCAN_S;
````


## -struct-fields
<dl>

### -field <b>EventData</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a> that specifies the standard event structure, which contains the event handle that the driver notifies about the scan operation. </p>
</dd>

### -field <b>StartFrequency</b>

<dd>
<p>The initial frequency, in Hz, for a scan operation. </p>
</dd>

### -field <b>EndFrequency</b>

<dd>
<p>The final frequency, in Hz, for a scan operation.  </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559566">EVENTSETID_TUNER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561898">KSEVENT_TUNER_INITIATE_SCAN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSEVENT_TUNER_INITIATE_SCAN_S structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
