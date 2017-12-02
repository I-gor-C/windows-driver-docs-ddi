---
UID: NS.pepfx._PEP_WORK_POWER_CONTROL
title: PEP_WORK_POWER_CONTROL
author: windows-driver-content
description: The PEP_WORK_POWER_CONTROL structure contains the parameters for a power control request that the platform extension plug-in (PEP) sends directly to a processor driver.
old-location: kernel\pep_work_power_control.htm
old-project: kernel
ms.assetid: 84258422-A2AE-449F-97C8-41336FEA5D8B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_WORK_POWER_CONTROL, PEP_WORK_POWER_CONTROL, *PPEP_WORK_POWER_CONTROL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_WORK_POWER_CONTROL
req.alt-loc: pepfx.h
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

# PEP_WORK_POWER_CONTROL structure



## -description
<p>The <b>PEP_WORK_POWER_CONTROL</b> structure contains the parameters for a <a href="kernel.ppm_power_control_codes">power control request</a> that the platform extension plug-in (PEP) sends directly to a processor driver.</p>


## -syntax

````
typedef struct _PEP_WORK_POWER_CONTROL {
  POHANDLE DeviceHandle;
  LPCGUID  PowerControlCode;
  PVOID    RequestContext;
  PVOID    InBuffer;
  SIZE_T   InBufferSize;
  PVOID    OutBuffer;
  SIZE_T   OutBufferSize;
} PEP_WORK_POWER_CONTROL, *PPEP_WORK_POWER_CONTROL;
````


## -struct-fields
<dl>

### -field DeviceHandle

<dd>
<p>A POHANDLE value that identifies the processor. The PEP received this handle in a previous <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification.</p>
</dd>

### -field PowerControlCode

<dd>
<p>[in] A pointer to a <a href="http://msdn.microsoft.com/library/windows/desktop/aa373931(v=vs.85).aspx">GUID</a> value that specifies the power control operation to perform.</p>
</dd>

### -field RequestContext

<dd>
<p>A pointer to a PEP-defined context value. The PEP might use this value to uniquely identify a power control request message (in case the PEP issues multiple requests with the same control code to the same device).</p>
</dd>

### -field InBuffer

<dd>
<p>[in] A pointer to a driver-allocated input buffer that contains the input parameters for this power control operation.</p>
</dd>

### -field InBufferSize

<dd>
<p>[in] The size in bytes of the buffer pointed to by <b>InBuffer</b>.</p>
</dd>

### -field OutBuffer

<dd>
<p>[in] A pointer to a driver-allocated output buffer to which the PEP writes the results of this power control operation.</p>
</dd>

### -field OutBufferSize

<dd>
<p>[in] The size in bytes of the buffer pointed to by <b>OutBuffer</b>.</p>
</dd>
</dl>

## -remarks
<p>The <b>PowerControl</b> member of the <a href="..\pepfx\ns-pepfx--pep-work-information.md">PEP_WORK_INFORMATION</a> structure is a pointer to a <b>PEP_WORK_POWER_CONTROL</b> structure.</p>

<p>The PEP issues a power control request from a worker thread. The Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) forwards this request by calling the processor driver's <a href="kernel.powercontrolcallback">PowerControlCallback</a> routine, if the driver implements this routine.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="http://msdn.microsoft.com/library/windows/desktop/aa373931(v=vs.85).aspx">GUID</a></dt>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-work-information.md">PEP_WORK_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pofxregisterdevice.md">PoFxRegisterDevice</a>
</dt>
<dt>
<a href="kernel.powercontrolcallback">PowerControlCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_WORK_POWER_CONTROL structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
