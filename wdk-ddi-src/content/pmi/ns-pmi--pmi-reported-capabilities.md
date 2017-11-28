---
UID: NS.pmi._PMI_REPORTED_CAPABILITIES
title: PMI_REPORTED_CAPABILITIES
author: windows-driver-content
description: The PMI_REPORTED_CAPABILITIES structure contains information about the type of power metering and budgeting capabilities a power meter supports. Additionally, this structure contains asset information about the power meter itself.
old-location: powermeter\pmi_reported_capabilities.htm
old-project: powermeter
ms.assetid: bcb0eb53-e3b3-4cec-9912-6306e8faef21
ms.author: windowsdriverdev
ms.date: 11/6/2017
ms.keywords: PMI_REPORTED_CAPABILITIES, PMI_REPORTED_CAPABILITIES, *PPMI_REPORTED_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pmi.h
req.include-header: Pmi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PMI_REPORTED_CAPABILITIES
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
req.irql: 
req.iface: 
---

# PMI_REPORTED_CAPABILITIES structure



## -description
<p>The PMI_REPORTED_CAPABILITIES structure contains information about the type of power metering and budgeting capabilities a power meter supports. Additionally, this structure contains asset information about the power meter itself.</p>


## -syntax

````
typedef struct _PMI_REPORTED_CAPABILITIES {
  ULONG                Flags;
  PMI_MEASUREMENT_UNIT MeasurementUnit;
  PMI_MEASUREMENT_TYPE MeasurementType;
  ULONG                Accuracy;
  ULONG                SamplingPeriod;
  ULONG                MinimumAverageInterval;
  ULONG                MaximumAverageInterval;
  ULONG                Hysteresis;
  BOOLEAN              Writeable;
  ULONG                MinBudget;
  ULONG                MaxBudget;
  WCHAR                ModelNumber[PMI_NAME_MAX];
  WCHAR                SerialNumber[PMI_NAME_MAX];
  WCHAR                OEMInformation[PMI_NAME_MAX];
} PMI_REPORTED_CAPABILITIES, *PPMI_REPORTED_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>A bitmask that specifies the supported capabilities of the power meter. The following flags define the range of values for this member:</p>
<p></p>
<dl>

### -field <a id="PMI_CAPABILITIES_SUPPORT_MEASUREMENT"></a><a id="pmi_capabilities_support_measurement"></a>PMI_CAPABILITIES_SUPPORT_MEASUREMENT

<dd>
<p>This bit is set if the power meter supports power measurement.</p>
</dd>

### -field <a id="PMI_CAPABILITIES_SUPPORT_THRESHOLDS"></a><a id="pmi_capabilities_support_thresholds"></a>PMI_CAPABILITIES_SUPPORT_THRESHOLDS

<dd>
<p>This bit is set if the power meter supports power thresholds.</p>
</dd>

### -field <a id="PMI_CAPABILITIES_SUPPORT_BUDGETING"></a><a id="pmi_capabilities_support_budgeting"></a>PMI_CAPABILITIES_SUPPORT_BUDGETING

<dd>
<p>This bit is set if the power meter supports power budgeting.</p>
</dd>

### -field <a id="PMI_CAPABILITIES_DISCHARGE_ONLY"></a><a id="pmi_capabilities_discharge_only"></a>PMI_CAPABILITIES_DISCHARGE_ONLY

<dd>
<p>This bit is set if the power meter reports data only when the power supply is discharging. This is typically the case on mobile battery systems or some uninterruptible power supplies (UPSs).</p>
</dd>
</dl>
</dd>

### -field <b>MeasurementUnit</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff543897">PMI_MEASUREMENT_UNIT</a> enumeration value that specifies the measurement unit. </p>
<div class="alert"><b>Note</b>  Beginning with Windows 7, Windows Server 2008 R2, only measurement units of milliwatts (mW) are supported.</div>
<div> </div>
</dd>

### -field <b>MeasurementType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff543895">PMI_MEASUREMENT_TYPE</a> enumeration value that specifies the measurement type, such as whether input or output power is measured.</p>
</dd>

### -field <b>Accuracy</b>

<dd>
<p>A value, in units of thousandths of a percent, that specifies the reported accuracy of the power meter. For example, a value of 1,000 corresponds to a one percent accuracy rating.</p>
</dd>

### -field <b>SamplingPeriod</b>

<dd>
<p>A value, in units of milliseconds, that specifies the current averaging period.</p>
</dd>

### -field <b>MinimumAverageInterval</b>

<dd>
<p>A value, in units of milliseconds, that specifies the minimum averaging interval.</p>
</dd>

### -field <b>MaximumAverageInterval</b>

<dd>
<p>A value, in units of milliseconds, that specifies the maximum averaging interval.</p>
</dd>

### -field <b>Hysteresis</b>

<dd>
<p>A value, in units of milliseconds, that specifies the hysteresis value. This value indicates the margin that is built around the threshold and budget events. This value prevents the trigger of unnecessary events when the reading fluctuates very close to one of the thresholds.</p>
</dd>

### -field <b>Writeable</b>

<dd>
<p>A Boolean value that indicates whether the budgeting information is read/write (TRUE) or read-only (FALSE).</p>
</dd>

### -field <b>MinBudget</b>

<dd>
<p>A value, in units of watts, that specifies the minimum supported power budget.</p>
</dd>

### -field <b>MaxBudget</b>

<dd>
<p>A value, in units of watts, that specifies the maximum supported power budget.</p>
</dd>

### -field <b>ModelNumber</b>

<dd>
<p>A null-terminated, Unicode string that contains the model number of the power meter.</p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>A null-terminated, Unicode string that contains the serial number of the power meter.</p>
</dd>

### -field <b>OEMInformation</b>

<dd>
<p>A null-terminated, Unicode string that contains descriptive information about the power meter. This information is specific to the implementation by the original OEM.</p>
</dd>
</dl>

## -remarks
<p>The PMI_REPORTED_CAPABILITIES structure contains the following information about a power meter:</p>

<p>The power meter's measurement capabilities.</p>

<p>The power meter's budget capabilities, which includes whether the budget configuration can be changed.</p>

<p>The power meter's asset information. This information is defined by the OEM for the power meter.</p>

<p>The PMI_REPORTED_CAPABILITIES structure is returned through an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543837">IOCTL_PMI_GET_CAPABILITIES</a> I/O control (IOCTL) query request. The input data for this query request is set to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543864">PMI_CAPABILITIES_TYPE</a> enumerator value of <b>PmiReportedCapabilities</b>..</p>

<p>If the query request completes successfully, the request returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543859">PMI_CAPABILITIES</a> structure. The <b>Capabilities</b> member of this structure is formatted as a PMI_REPORTED_CAPABILITIES structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543837">IOCTL_PMI_GET_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543859">PMI_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543864">PMI_CAPABILITIES_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20PMI_REPORTED_CAPABILITIES structure%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
