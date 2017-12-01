---
UID: NF.storport.StorPortPoFxPowerControl
title: StorPortPoFxPowerControl
author: windows-driver-content
description: The StorPortPoFxPowerControl routine sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP).
old-location: storage\storportpofxpowercontrol.htm
old-project: storage
ms.assetid: 1EBEBD5D-E0E5-48A3-8CDA-C336575E53C6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortPoFxPowerControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortPoFxPowerControl
req.alt-loc: storport.lib,storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortPoFxPowerControl function



## -description
<p>The <b>StorPortPoFxPowerControl</b> routine sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP).</p>


## -syntax

````
ULONG StorPortPoFxPowerControl(
  _In_      PVOID   HwDeviceExtension,
  _In_      LPCGUID PowerControlCode,
  _In_opt_  PVOID   InBuffer,
  _In_      SIZE_T  InBufferSize,
  _Out_opt_ PVOID   OutBuffer,
  _In_      SIZE_T  OutBufferSize,
  _Out_opt_ PSIZE_T BytesReturned
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA). This is the device extension used to register the device in a prior call to <a href="..\storport\nf-storport-storportinitializepofxpower.md">StorPortInitializePoFxPower</a>.</p>
</dd>

### -param <i>PowerControlCode</i> [in]

<dd>
<p>A pointer to the power control code. This code is a GUID value that specifies the requested operation.</p>
</dd>

### -param <i>InBuffer</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated buffer that contains the input data for the operation. The format for the data in this buffer depends on the power control code specified by the <i>PowerControlCode</i> parameter. The <i>InBuffer</i> parameter is optional and can be specified as NULL if the specified operation requires no input data.</p>
</dd>

### -param <i>InBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the input buffer that is pointed to by the <i>InBuffer</i> parameter. If <i>InBuffer</i> is NULL, set <i>InBufferSize</i> to zero.</p>
</dd>

### -param <i>OutBuffer</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer that is to contain the output data from the operation. The format for the data in this buffer depends on the power control code specified by the <i>PowerControlCode</i> parameter. The <i>OutBuffer</i> parameter is optional and can be specified as NULL if the specified operation produces no output data.</p>
</dd>

### -param <i>OutBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the output buffer that is pointed to by the <i>OutBuffer</i> parameter. If <i>OutBuffer</i> is NULL, set <i>OutBufferSize</i> to zero.</p>
</dd>

### -param <i>BytesReturned</i> [out, optional]

<dd>
<p>A pointer to a location into which the routine writes the number of bytes of data that were written to the buffer that is pointed to by <i>OutBuffer</i>. The number of bytes written will be less than or equal to <i>OutBufferSize</i>. This parameter is optional and can be specified as <b>NULL</b> if the caller does not need to know how many bytes were written to the output buffer.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortPoFxPowerControl</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The power control operation specified in <i>PowerControlCode</i> was successfully executed.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either <i>HwDeviceExtension</i> or <i>Device</i> is NULL.</p>

<p>-or-</p>

<p><i>Address</i> points to an invalid unit address structure.</p>

<p>-or-</p>

<p>The storage device specified by <i>Address</i> is not found.</p><dl>
<dt><b>STOR_STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The storage device is  not registered with the PoFx.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The current IRQL &gt; DISPATCH_LEVEL.</p><dl>
<dt><b>STOR_STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The power control operation was unsuccessful.</p>

<p> </p>

## -remarks
<p>A minport driver calls this routine to send a power control request directly to the PEP. A power control request is similar to an I/O control request (IOCTL). Unlike an IOCTL, however, a power control request is sent directly to PEP and is not observed by other device drivers in the device stack. During a <b>StorPortPoFxPowerControl</b> call, the PEP synchronously performs the requested operation.</p>

<p>Similarly, The PEP can send a power control request directly to the miniport. The miniport driver handles this request in its <a href="storage.hwstoradaptercontrol">HwStorAdapterControl</a> and <a href="storage.hwstorunitcontrol">HwStorUnitControl</a> routines. The <i>ControlType</i> parameter receives the <b>ScsiAdapterPoFxPowerControl</b> type in the <b>HwStorAdapterControl</b> routine and the <b>ScsiUnitPoFxPowerControl</b> in the <b>HwStorUnitControl</b> routine.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hwstoradaptercontrol">HwStorAdapterControl</a>
</dt>
<dt>
<a href="storage.hwstorunitcontrol">HwStorUnitControl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortPoFxPowerControl routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
