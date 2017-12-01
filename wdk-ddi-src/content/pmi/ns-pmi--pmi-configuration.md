---
UID: NS.pmi._PMI_CONFIGURATION
title: PMI_CONFIGURATION
author: windows-driver-content
description: The PMI_CONFIGURATION structure contains information about the current power metering and budgeting configuration of a power meter.
old-location: powermeter\pmi_configuration.htm
old-project: powermeter
ms.assetid: 976b812e-deb2-445f-b69d-e00d10c6e5d8
ms.author: windowsdriverdev
ms.date: 11/6/2017
ms.keywords: PMI_CONFIGURATION, PMI_CONFIGURATION, *PPMI_CONFIGURATION
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
req.alt-api: PMI_CONFIGURATION
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

# PMI_CONFIGURATION structure



## -description
<p>The PMI_CONFIGURATION structure contains information about the current power metering and budgeting configuration of a power meter.</p>


## -syntax

````
typedef struct _PMI_CONFIGURATION {
  ULONG                  Version;
  USHORT                 Size;
  PMI_CONFIGURATION_TYPE ConfigurationType;
  union {
    PMI_MEASUREMENT_CONFIGURATION MeasurementConfiguration;
    PMI_BUDGETING_CONFIGURATION   BudgetingConfiguration;
    PMI_THRESHOLD_CONFIGURATION   ThresholdConfiguration;
  } Configuration;
} PMI_CONFIGURATION, *PPMI_CONFIGURATION;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>A value that specifies the version of this structure. For Windows 7, Windows Server 2008 R2, and later versions of Windows, this value must be 1.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>A value, in units of bytes, that specifies the size of the structure.</p>
</dd>

### -field <b>ConfigurationType</b>

<dd>
<p>A <a href="..\pmi\ne-pmi-pmi-configuration-type.md">PMI_CONFIGURATION_TYPE</a> enumeration value that specifies the data type of the <b>Configuration</b> member.</p>
</dd>

### -field <b>Configuration</b>

<dd>
<p>A union of the supported Power Meter Interface (PMI) configuration structures. Based on the value of the <b>ConfigurationType</b> member, one of the following <b>Configuration</b> submembers is used to reference the following PMI configuration structures:</p>
<dl>

### -field <b>MeasurementConfiguration</b>

<dd>
<p>A <a href="..\pmi\ns-pmi--pmi-budgeting-configuration.md">PMI_BUDGETING_CONFIGURATION</a> structure that contains information about the budgeting configuration of the power meter.</p>
<p>The <b>Configuration</b> member contains this structure if the <b>ConfigurationType</b> member is set to <b>PmiBudgetingConfiguration</b>.</p>
</dd>

### -field <b>BudgetingConfiguration</b>

<dd>
<p>A <a href="..\pmi\ns-pmi--pmi-measurement-configuration.md">PMI_MEASUREMENT_CONFIGURATION</a> structure that contains information about the measurement configuration of the power meter.</p>
<p>The <b>Configuration</b> member contains this structure if the <b>ConfigurationType</b> member is set to <b>PmiMeasurementConfiguration</b>.</p>
</dd>

### -field <b>ThresholdConfiguration</b>

<dd>
<p>A <a href="..\pmi\ns-pmi--pmi-threshold-configuration.md">PMI_THRESHOLD_CONFIGURATION</a> structure that contains information about the threshold configuration of the power meter.</p>
<p>The <b>Configuration</b> member contains this structure if the <b>ConfigurationType</b> member is set to <b>PmiThresoldConfiguration</b>.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The PMI_CONFIGURATION structure is used to query many different PMI configuration settings that are supported by a power meter. </p>

<p>The PMI configuration information is returned through an <a href="..\pmi\ni-pmi-ioctl-pmi-get-configuration.md">IOCTL_PMI_GET_CONFIGURATION</a> I/O control (IOCTL) query request. The input data of this query request is set to a <a href="..\pmi\ne-pmi-pmi-configuration-type.md">PMI_CONFIGURATION_TYPE</a> enumerator value that specifies the type of PMI configuration data to return.</p>

<p>If the IOCTL query request completes successfully, the request returns a PMI_CONFIGURATION structure. The <b>Configuration</b> member of this structure contains data that is formatted as the requested PMI configuration structure.</p>

<p>For example, if an IOCTL query request of <a href="..\pmi\ni-pmi-ioctl-pmi-get-configuration.md">IOCTL_PMI_GET_CONFIGURATION</a> is made with the input data set to <b>PmiBudgetingConfiguration</b> and the request completes successfully, the request returns a PMI_CONFIGURATION structure with its members set to the following values:</p>

<p>The <b>ConfigurationType</b> member is set to <b>PmiBudgetingConfiguration</b>.</p>

<p>The <b>Configuration</b> member contains data that is  formatted as a <a href="..\pmi\ns-pmi--pmi-budgeting-configuration.md">PMI_BUDGETING_CONFIGURATION</a> structure.</p>

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
<a href="..\pmi\ni-pmi-ioctl-pmi-get-configuration.md">IOCTL_PMI_GET_CONFIGURATION</a>
</dt>
<dt>
<a href="..\pmi\ns-pmi--pmi-budgeting-configuration.md">PMI_BUDGETING_CONFIGURATION</a>
</dt>
<dt>
<a href="..\pmi\ne-pmi-pmi-configuration-type.md">PMI_CONFIGURATION_TYPE</a>
</dt>
<dt>
<a href="..\pmi\ns-pmi--pmi-measurement-configuration.md">PMI_MEASUREMENT_CONFIGURATION</a>
</dt>
<dt>
<a href="..\pmi\ns-pmi--pmi-threshold-configuration.md">PMI_THRESHOLD_CONFIGURATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20PMI_CONFIGURATION structure%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
