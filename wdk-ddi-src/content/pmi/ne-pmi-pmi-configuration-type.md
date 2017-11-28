---
UID: NE.pmi.PMI_CONFIGURATION_TYPE
title: PMI_CONFIGURATION_TYPE
author: windows-driver-content
description: The PMI_CONFIGURATION_TYPE enumeration defines the type of PMI configuration data that is referenced by the Configuration member of the PMI_CONFIGURATION structure.
old-location: powermeter\pmi_configuration_type.htm
old-project: powermeter
ms.assetid: d5ffd580-ca3d-46c7-b0ba-1cd9962517f8
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
req.alt-api: PMI_CONFIGURATION_TYPE
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

# PMI_CONFIGURATION_TYPE enumeration



## -description
<p>The PMI_CONFIGURATION_TYPE enumeration defines the type of PMI configuration data that is referenced by the <b>Configuration</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543865">PMI_CONFIGURATION</a> structure. This enumeration is also used to specify the type of <a href="https://msdn.microsoft.com/library/windows/hardware/ff543859">PMI_CAPABILITIES</a> structure to return through an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543842">IOCTL_PMI_GET_CONFIGURATION</a> I/O control (IOCTL) request.</p>


## -syntax

````
typedef enum  { 
  PmiMeasurementConfiguration,
  PmiBudgetingConfiguration,
  PmiThresholdConfiguration,
  PmiConfigurationMax
} PMI_CONFIGURATION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PmiMeasurementConfiguration"></a><a id="pmimeasurementconfiguration"></a><a id="PMIMEASUREMENTCONFIGURATION"></a><b>PmiMeasurementConfiguration</b>

<dd>
<p>The PMI configuration data, formatted as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543887">PMI_MEASUREMENT_CONFIGURATION</a> structure, contains information about the measurement configuration of the power meter.</p>
</dd>

### -field <a id="PmiBudgetingConfiguration"></a><a id="pmibudgetingconfiguration"></a><a id="PMIBUDGETINGCONFIGURATION"></a><b>PmiBudgetingConfiguration</b>

<dd>
<p>The PMI configuration data, formatted as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543858">PMI_BUDGETING_CONFIGURATION</a> structure, contains information about the budgeting configuration of the power meter.</p>
</dd>

### -field <a id="PmiThresholdConfiguration"></a><a id="pmithresholdconfiguration"></a><a id="PMITHRESHOLDCONFIGURATION"></a><b>PmiThresholdConfiguration</b>

<dd>
<p>The PMI configuration data, formatted as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543908">PMI_THRESHOLD_CONFIGURATION</a> structure, contains information about the budgeting configuration of the power meter.</p>
</dd>

### -field <a id="PmiConfigurationMax"></a><a id="pmiconfigurationmax"></a><a id="PMICONFIGURATIONMAX"></a><b>PmiConfigurationMax</b>

<dd>
<p>The maximum number of PMI configuration structures.</p>
</dd>
</dl>

## -remarks
<p>The <b>ConfigurationType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543865">PMI_CONFIGURATION</a> structure contains information about the type of PMI configuration data that is referenced by the <b>Configuration</b> member of that structure. This structure is returned through a successful completion of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543842">IOCTL_PMI_GET_CONFIGURATION</a> IOCTL request and is passed in the input buffer for an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543849">IOCTL_PMI_SET_CONFIGURATION</a> IOCTL request.</p>

<p>The <b>ConfigurationType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543865">PMI_CONFIGURATION</a> structure contains information about the type of PMI configuration data that is referenced by the <b>Configuration</b> member of that structure. This structure is returned through a successful completion of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543842">IOCTL_PMI_GET_CONFIGURATION</a> IOCTL request and is passed in the input buffer for an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543849">IOCTL_PMI_SET_CONFIGURATION</a> IOCTL request.</p>

<p>The <b>ConfigurationType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543865">PMI_CONFIGURATION</a> structure contains information about the type of PMI configuration data that is referenced by the <b>Configuration</b> member of that structure. This structure is returned through a successful completion of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543842">IOCTL_PMI_GET_CONFIGURATION</a> IOCTL request and is passed in the input buffer for an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543849">IOCTL_PMI_SET_CONFIGURATION</a> IOCTL request.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543842">IOCTL_PMI_GET_CONFIGURATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543849">IOCTL_PMI_SET_CONFIGURATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543858">PMI_BUDGETING_CONFIGURATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543865">PMI_CONFIGURATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543887">PMI_MEASUREMENT_CONFIGURATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543908">PMI_THRESHOLD_CONFIGURATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20PMI_CONFIGURATION_TYPE enumeration%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
