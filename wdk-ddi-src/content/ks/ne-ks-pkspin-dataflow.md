---
UID: NE.ks.PKSPIN_DATAFLOW
title: PKSPIN_DATAFLOW
author: windows-driver-content
description: An instance of the KSPIN_DATAFLOW enumeration is returned by KSPROPERTY_PIN_DATAFLOW.
old-location: stream\kspin_dataflow.htm
old-project: stream
ms.assetid: feab830d-8079-4051-8974-52905f845765
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPIN_DATAFLOW
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

# PKSPIN_DATAFLOW enumeration



## -description
<p>An instance of the KSPIN_DATAFLOW enumeration is returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff565197">KSPROPERTY_PIN_DATAFLOW</a>.</p>


## -syntax

````
typedef enum  { 
  KSPIN_DATAFLOW_IN   = 1,
  KSPIN_DATAFLOW_OUT  = 2
} KSPIN_DATAFLOW, *PKSPIN_DATAFLOW;
````


## -enum-fields
<dl>

### -field <a id="KSPIN_DATAFLOW_IN"></a><a id="kspin_dataflow_in"></a><b>KSPIN_DATAFLOW_IN</b>

<dd>
<p>Indicates that the pin factory instantiates data sink pins. Such pins can only be connected to data source pins. </p>
</dd>

### -field <a id="KSPIN_DATAFLOW_OUT"></a><a id="kspin_dataflow_out"></a><b>KSPIN_DATAFLOW_OUT</b>

<dd>
<p>Indicates that the pin factory instantiates data source pins. Such pins can only be connected to data sink pins.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563533">KSPIN_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559692">HW_STREAM_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPIN_DATAFLOW enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
