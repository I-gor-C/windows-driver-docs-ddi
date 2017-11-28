---
UID: NF.wdm.PoFxPowerControl
title: PoFxPowerControl
author: windows-driver-content
description: The PoFxPowerControl routine sends a power control request to the power management framework (PoFx).
old-location: kernel\pofxpowercontrol.htm
old-project: kernel
ms.assetid: B821AF54-AF2C-4E19-BC70-2E0A8F172D93
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PoFxPowerControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxPowerControl
req.alt-loc: Ntoskrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Ntoskrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PoFxPowerControl function



## -description
<p>The <b>PoFxPowerControl</b> routine sends a power control request to the power management framework (PoFx).</p>


## -syntax

````
NTSTATUS PoFxPowerControl(
  _In_      POHANDLE Handle,
  _In_      LPCGUID  PowerControlCode,
  _In_opt_  PVOID    InBuffer,
  _In_      SIZE_T   InBufferSize,
  _Out_opt_ PVOID    OutBuffer,
  _In_      SIZE_T   OutBufferSize,
  _Out_opt_ PSIZE_T  BytesReturned
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>A handle that represents the registration of the device with PoFx. The device driver previously received this handle from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a> routine.</p>
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
<p><b>PoFxPowerControl</b> returns <b>STATUS_SUCCESS</b> if the requested operation succeeds. Possible error return values include the following status code.</p><dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>The requested power control operation is not implemented.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The power engine plug-in (PEP) does not acknowledge support for this device.</p>

<p> </p>

## -remarks
<p>A device driver calls this routine to send a power control request directly to PoFx. A power control request is similar to an I/O control request (IOCTL). Unlike an IOCTL, however, a power control request is sent directly to PoFx and is not observed by other device drivers in the device stack. During a <b>PoFxPowerControl</b> call, PoFx synchronously performs the requested operation.</p>

<p>Similarly, PoFx can send a power control request directly to the device driver. The driver handles this request in its <a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a> routine.</p>

<p>PoFx delegates the handling of all power control requests to the power engine plug-in (PEP). The PEP is an optional software component that performs power management tasks that are specific to a particular product line of processor or System on a Chip (SoC) modules. If the hardware vendor for the processor or SoC supplies a PEP for a hardware platform, this PEP might handle custom power control requests from a device driver, or might send custom power control requests to the driver's <i>PowerControlCallback</i> routine. The vendor can specify a set of <i>PowerControlCode</i> GUIDs and define the operations that are designated by these GUIDs. As an option, a device driver can contain platform-specific code to handle or to send requests for these operations.</p>

<p>A device driver calls this routine to send a power control request directly to PoFx. A power control request is similar to an I/O control request (IOCTL). Unlike an IOCTL, however, a power control request is sent directly to PoFx and is not observed by other device drivers in the device stack. During a <b>PoFxPowerControl</b> call, PoFx synchronously performs the requested operation.</p>

<p>Similarly, PoFx can send a power control request directly to the device driver. The driver handles this request in its <a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a> routine.</p>

<p>PoFx delegates the handling of all power control requests to the power engine plug-in (PEP). The PEP is an optional software component that performs power management tasks that are specific to a particular product line of processor or System on a Chip (SoC) modules. If the hardware vendor for the processor or SoC supplies a PEP for a hardware platform, this PEP might handle custom power control requests from a device driver, or might send custom power control requests to the driver's <i>PowerControlCallback</i> routine. The vendor can specify a set of <i>PowerControlCode</i> GUIDs and define the operations that are designated by these GUIDs. As an option, a device driver can contain platform-specific code to handle or to send requests for these operations.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.exe</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxPowerControl routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
