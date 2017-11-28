---
UID: NE.pmi.PMI_EVENT_TYPE
title: PMI_EVENT_TYPE
author: windows-driver-content
description: The PMI_EVENT_TYPE enumeration defines the type of PMI power meter event that is returned through the successful completion of an IOCTL_PMI_REGISTER_EVENT_NOTIFY request.
old-location: powermeter\pmi_event_type.htm
old-project: powermeter
ms.assetid: c2a8422d-15f0-45df-bc54-946fb3d11a22
ms.author: windowsdriverdev
ms.date: 11/6/2017
ms.keywords: PEP_WORK_IDLE_STATE, PEP_WORK_IDLE_STATE, *PPEP_WORK_IDLE_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pmi.h
req.include-header: Pmi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PMI_EVENT_TYPE
req.alt-loc: pmi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PMI_EVENT_TYPE enumeration



## -description
<p>The PMI_EVENT_TYPE enumeration defines the type of PMI power meter event that is returned through the successful completion of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543847">IOCTL_PMI_REGISTER_EVENT_NOTIFY</a> request.</p>


## -syntax

````
typedef enum  { 
  PmiCapabilitiesChangedEvent,
  PmiThresholdEvent,
  PmiConfigurationChangedEvent,
  PmiBudgetEvent,
  PmiAveragingIntervalChangedEvent,
  PmiEventMax
} PMI_EVENT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PmiCapabilitiesChangedEvent"></a><a id="pmicapabilitieschangedevent"></a><a id="PMICAPABILITIESCHANGEDEVENT"></a><b>PmiCapabilitiesChangedEvent</b>

<dd>
<p>The event was caused by a change in the PMI capabilities of the power meter.</p>
</dd>

### -field <a id="PmiThresholdEvent"></a><a id="pmithresholdevent"></a><a id="PMITHRESHOLDEVENT"></a><b>PmiThresholdEvent</b>

<dd>
<p>The event was caused because the power level exceeded a configured threshold of the power meter.</p>
</dd>

### -field <a id="PmiConfigurationChangedEvent"></a><a id="pmiconfigurationchangedevent"></a><a id="PMICONFIGURATIONCHANGEDEVENT"></a><b>PmiConfigurationChangedEvent</b>

<dd>
<p>The event was caused by a change in the PMI configuration of the power meter.</p>
</dd>

### -field <a id="PmiBudgetEvent"></a><a id="pmibudgetevent"></a><a id="PMIBUDGETEVENT"></a><b>PmiBudgetEvent</b>

<dd>
<p>The event was caused because the power budget exceeded or fell below the configured budget of the power meter.</p>
</dd>

### -field <a id="PmiAveragingIntervalChangedEvent"></a><a id="pmiaveragingintervalchangedevent"></a><a id="PMIAVERAGINGINTERVALCHANGEDEVENT"></a><b>PmiAveragingIntervalChangedEvent</b>

<dd>
<p>The event was caused because the interval, during which the power meter averages power measurement data, was changed.</p>
</dd>

### -field <a id="PmiEventMax"></a><a id="pmieventmax"></a><a id="PMIEVENTMAX"></a><b>PmiEventMax</b>

<dd>
<p>The maximum number of PMI event types.</p>
</dd>
</dl>

## -remarks
<p>The <b>EventType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543876">PMI_EVENT</a> structure contains information about the type of PMI event data that is referenced by the <b>Event</b> member of that structure. This structure is returned through a successful completion of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543847">IOCTL_PMI_REGISTER_EVENT_NOTIFY</a> request.</p>

<p>The <b>EventType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543876">PMI_EVENT</a> structure contains information about the type of PMI event data that is referenced by the <b>Event</b> member of that structure. This structure is returned through a successful completion of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543847">IOCTL_PMI_REGISTER_EVENT_NOTIFY</a> request.</p>

<p>The <b>EventType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543876">PMI_EVENT</a> structure contains information about the type of PMI event data that is referenced by the <b>Event</b> member of that structure. This structure is returned through a successful completion of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543847">IOCTL_PMI_REGISTER_EVENT_NOTIFY</a> request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pmi.h (include Pmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543847">IOCTL_PMI_REGISTER_EVENT_NOTIFY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543876">PMI_EVENT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20PMI_EVENT_TYPE enumeration%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
