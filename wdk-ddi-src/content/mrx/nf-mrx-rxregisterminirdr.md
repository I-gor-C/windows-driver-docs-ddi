---
UID: NF.mrx.RxRegisterMinirdr
title: RxRegisterMinirdr
author: windows-driver-content
description: RxRegisterMinirdr is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector.
old-location: ifsk\rxregisterminirdr.htm
old-project: ifsk
ms.assetid: f9c2fedd-b513-4ea9-b915-cdcc05b88d6f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxRegisterMinirdr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxRegisterMinirdr
req.alt-loc: mrx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# RxRegisterMinirdr function



## -description
<p><b>RxRegisterMinirdr</b> is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector. </p>


## -syntax

````
NTSTATUS RxRegisterMinirdr(
  _Out_   PRDBSS_DEVICE_OBJECT *DeviceObject,
  _Inout_ PDRIVER_OBJECT       DriverObject,
  _In_    PMINIRDR_DISPATCH    MrdrDispatch,
  _In_    ULONG                Controls,
  _In_    PUNICODE_STRING      DeviceName,
  _In_    ULONG                DeviceExtensionSize,
  _In_    DEVICE_TYPE          DeviceType,
  _In_    ULONG                DeviceCharacteristics
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [out]

<dd>
<p>A pointer to where the created device object will be stored.</p>
</dd>

### -param <i>DriverObject</i> [in, out]

<dd>
<p>A pointer to the driver object of the network mini-redirector driver. Each driver receives a pointer to its driver object in a parameter to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. This driver object will be used to create the device object for the network mini-redirector driver. </p>
</dd>

### -param <i>MrdrDispatch</i> [in]

<dd>
<p>A pointer to the dispatch table for the network mini-redirector. This dispatch table includes configuration information for the network mini-redirector and a table of pointers to callback routines implemented by the network mini-redirector kernel driver. RDBSS makes calls to the network mini-redirector driver through this list of callback routines. </p>
</dd>

### -param <i>Controls</i> [in]

<dd>
<p>The set of options that determine capabilities of the network mini-redirector driver and how RDBSS should handle initialization and name table caching for the network mini-redirector driver. These options can include any combination of the following bits:</p>
<p></p>
<dl>

### -param <a id="RX_REGISTERMINI_FLAG_DONT_PROVIDE_UNCS"></a><a id="rx_registermini_flag_dont_provide_uncs"></a>RX_REGISTERMINI_FLAG_DONT_PROVIDE_UNCS

<dd>
<p>When this flag is set, it indicates that the network mini-redirector does not support UNC names.</p>
</dd>

### -param <a id="RX_REGISTERMINI_FLAG_DONT_PROVIDE_MAILSLOTS"></a><a id="rx_registermini_flag_dont_provide_mailslots"></a>RX_REGISTERMINI_FLAG_DONT_PROVIDE_MAILSLOTS

<dd>
<p>When this flag is set, it indicates that the network mini-redirector does not support mailslots.</p>
</dd>

### -param <a id="RX_REGISTERMINI_FLAG_DONT_INIT_DRIVER_DISPATCH"></a><a id="rx_registermini_flag_dont_init_driver_dispatch"></a>RX_REGISTERMINI_FLAG_DONT_INIT_DRIVER_DISPATCH

<dd>
<p>When this flag is set, it indicates that the network mini-redirector does not want RDBSS to initialize the driver dispatch entry points of the mini-redirector driver to point to RDBSS internal routines. This option would only be used in unusual circumstances. Normally RDBSS would set the driver dispatch entry points and the fast I/O dispatch in the network mini-redirector driver object to point to routines internal to RDBSS.</p>
</dd>

### -param <a id="RX_REGISTERMINI_FLAG_DONT_INIT_PREFIX_N_SCAVENGER"></a><a id="rx_registermini_flag_dont_init_prefix_n_scavenger"></a>RX_REGISTERMINI_FLAG_DONT_INIT_PREFIX_N_SCAVENGER

<dd>
<p>When this flag is set, it indicates that the network mini-redirector does not want RDBSS to initialize its internal network name table and scavenger data structures for scavenging this name table. This option would be set for a network mini-redirector that wants to handle caching for network share names itself and not use the RDBSS facilities for name caching and scavenging.</p>
</dd>
</dl>
</dd>

### -param <i>DeviceName</i> [in]

<dd>
<p>A pointer to a buffer that contains a zero-terminated Unicode string that names the device object. The string must be a full path name. This parameter is passed as <i>DeviceName</i> to the <b>IoCreateDevice</b> routine by RDBSS.</p>
</dd>

### -param <i>DeviceExtensionSize</i> [in]

<dd>
<p>The size specified by the mini-redirector driver for the number of bytes to be allocated for the device extension of the device object. The internal structure of the device extension is driver-defined. This parameter is added to the size of the device extension used by RDBSS and passed as the <i>DeviceExtensionSize</i> parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> routine by RDBSS.</p>
</dd>

### -param <i>DeviceType</i> [in]

<dd>
<p>The device type used when the device object is created. This specifies one of the system-defined FILE_DEVICE_XXX constants that indicate the type of device or a vendor-defined value for a new type of device. This value would normally be FILE_DEVICE_NETWORK_FILE_SYSTEM for network mini-redirector drivers. This parameter is passed as <i>DeviceType</i> to the <b>IoCreateDevice</b> routine by RDBSS. </p>
</dd>

### -param <i>DeviceCharacteristics</i> [in]

<dd>
<p>The device characteristics used when the device object is created. This specifies one or more system-defined constants, combined together, that provide additional information about the driver's device. This value must include FILE_REMOTE_DEVICE for network mini-redirector drivers, but this might be combined with other characteristics such as FILE_DEVICE_SECURE_OPEN. This parameter is passed as <i>DeviceCharacteristics</i> to the <b>IoCreateDevice</b> routine by RDBSS. </p>
</dd>
</dl>

## -returns
<p><b>RxRegisterMinirdr</b> returns STATUS_SUCCESS on success or one of the following error values on failure: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There were insufficient resources to create the device object.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was passed to the routine. This error will be returned if the <i>DeviceObject</i> parameter is a <b>NULL</b> pointer. </p><dl>
<dt><b>STATUS_OBJECT_NAME_COLLISION</b></dt>
</dl><p>A name collision occurred when trying to create this device object.</p><dl>
<dt><b>STATUS_OBJECT_NAME_EXISTS</b></dt>
</dl><p>A device object with this name already exists.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The call to create the device object returned a <b>NULL</b> device object.</p>

<p> </p>

## -remarks
<p>A network mini-redirector registers with RDBSS whenever the driver is loaded by the kernel and unregisters with RDBSS when the driver is unloaded. A non-monolithic driver (the SMB network mini-redirector) communicates with the <i>Rdbss.sys</i>, another kernel driver. For a monolithic network mini-redirector driver that statically links with <i>Rdbsslib.lib</i>, this communication is merely a call to an <i>Rdbsslib.lib</i> library routine.</p>

<p>A network mini-redirector informs RDBSS that it has been loaded by calling <b>RxRegisterMinirdr</b>, the registration routine exported from RDBSS. When a network mini-redirector driver first starts (in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine), the driver calls the RDBSS <b>RxRegisterMinirdr</b> routine to register the network mini-redirector driver with RDBSS. Based on the parameters passed to <b>RxRegisterMinirdr</b>, RDBSS calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> to create the device object for the network mini-redirector driver. </p>

<p>As part of this registration process, the network mini-redirector passes a parameter to <b>RxRegisterMinirdr</b> that is a pointer to a large structure, MINIRDR_DISPATCH, which contains configuration information for the network mini-redirector and a dispatch table of pointers to callback routines implemented by the network mini-redirector driver. This configuration data is used to configure internal RDBSS tables for use with this network mini-redirector. RDBSS uses the callback routines passed in this structure to communicate with the network mini-redirector. A network mini-redirector can chose to implement only some of these callback routines. Any callback routine that is not implemented should be set to a <b>NULL</b> pointer in the dispatch table passed to RDBSS. Only callback routines implemented by the network mini-redirector will be called by RDBSS. </p>

<p>Note that the <b>RxRegisterMinirdr</b> routine sets all of the driver dispatch routines of the network mini-redirector driver to point to the top-level RDBSS dispatch routine, <b>RxFsdDispatch</b>. A network mini-redirector can override this behavior by saving a copy of its driver dispatch entry points, calling <b>RxRegisterMinirdr</b>, and rewriting the driver dispatch with its own entry points after the call to <b>RxRegisterMinirdr</b> returns. A network mini-redirector can also prevent its driver dispatch routines from being copied over by the <b>RxRegisterMinirdr</b> routine if the RX_REGISTERMINI_FLAG_DONT_INIT_DRIVER_DISPATCH bit is set in the <i>Controls</i> parameter.</p>

<p>If the <b>RxRegisterMinirdr</b> call is successful, a number of members in RDBSS_DEVICE_OBJECT pointed to by the <i>DeviceObject</i> parameter are initialized including the following: </p>

<p>The <b>Dispatch</b> member is set to the <i>MrdrDispatch</i> parameter.</p>

<p>The <b>RegistrationControls</b> member is set to the <i>Controls</i> parameter.</p>

<p>The <b>DeviceName</b> member is set to the <i>DeviceName</i> parameter.</p>

<p>The <b>RegisterUncProvider</b> member is set to <b>TRUE</b> if the RX_REGISTERMINI_FLAG_DONT_PROVIDE_UNCS bit in the <i>Controls</i> parameter was not set.</p>

<p>The <b>RegisterMailSlotProvider</b> member is set to <b>TRUE</b> if the RX_REGISTERMINI_FLAG_DONT_PROVIDE_MAILSLOTS bit in the <i>Controls</i> parameter was not set.</p>

<p>The <b>NetworkProviderPriority</b> member is set to the network provider priority that MUP will use.</p>

<p>If the <b>RxRegisterMinirdr</b> call is successful and the RX_REGISTERMINI_FLAG_DONT_INIT_PREFIX_N_SCAVENGER bit in the <i>Controls</i> parameter is not set, a number of other members in RDBSS_DEVICE_OBJECT pointed to by the <i>DeviceObject</i> parameter are initialized, including the following: </p>

<p>The <b>pRxNetNameTable</b> member structure is initialized.</p>

<p>The <b>RxNetNameTableInDeviceObject.IsNetNameTable</b> member is set to <b>TRUE</b>.</p>

<p>The <b>pRdbssScavenger</b> member structure is initialized.</p>

<p>If the <b>RxRegisterMinirdr</b> call is successful, RDBSS sets the internal state of the network mini-redirector in RDBSS to RDBSS_STARTABLE.</p>

<p>The network mini-redirector does not actually start operation until it receives a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550829">MRxStart</a> routine, one of the callback routines passed in the MINIRDR_DISPATCH structure. The <b>MrxStart</b> callback routine must be implemented by the network mini-redirector driver if it wishes to receive callbacks for operations, unless the network mini-redirector preserves its own driver dispatch entry points. Otherwise, RDBSS will only allow the following I/O request packets through to the driver until <b>MrxStart</b> returns successfully:</p>

<p>IRP requests for device create operations and device operations where the <i>FileObject-&gt;FileName.Length</i> parameter on the IRPSP is zero and the <i>FileObject-&gt;RelatedFileObject</i> parameter is <b>NULL</b>.</p>

<p>For any other IRP request, the RDBSS dispatch routine, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554468">RxFsdDispatch</a>, will return a status of STATUS_REDIRECTOR_NOT_STARTED. </p>

<p>The RDBSS dispatch routine will also fail any requests for the following I/O request packets:</p>

<p>IRP_MJ_CREATE_MAILSLOT</p>

<p>IRP_MJ_CREATE_NAMED_PIPE</p>

<p>The network mini-redirector <b>MrxStart</b> routine is called by RDBSS when the <b>RxStartMiniRdr</b> routine is called. The RDBSS <b>RxStartMinirdr</b> is usually called as a result of an FSCTL or IOCTL request from a user-mode application or service to start the network mini-redirector. The call to <b>RxStartMinirdr </b>cannot be made from the <b>DriverEntry</b> routine of the network mini-redirector after a successful call to <b>RxRegisterMinirdr </b>because some of the start processing requires that the driver initialization be completed. Once the <b>RxStartMinirdr</b> call is received, RDBSS completes the start process by calling the <b>MrxStart</b> routine of the network mini-redirector. If the call to <b>MrxStart</b> returns success, RDBSS sets the internal state of the mini-redirector in RDBSS to RDBSS_STARTED. </p>

<p>A network mini-redirector registers with RDBSS whenever the driver is loaded by the kernel and unregisters with RDBSS when the driver is unloaded. A non-monolithic driver (the SMB network mini-redirector) communicates with the <i>Rdbss.sys</i>, another kernel driver. For a monolithic network mini-redirector driver that statically links with <i>Rdbsslib.lib</i>, this communication is merely a call to an <i>Rdbsslib.lib</i> library routine.</p>

<p>A network mini-redirector informs RDBSS that it has been loaded by calling <b>RxRegisterMinirdr</b>, the registration routine exported from RDBSS. When a network mini-redirector driver first starts (in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine), the driver calls the RDBSS <b>RxRegisterMinirdr</b> routine to register the network mini-redirector driver with RDBSS. Based on the parameters passed to <b>RxRegisterMinirdr</b>, RDBSS calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> to create the device object for the network mini-redirector driver. </p>

<p>As part of this registration process, the network mini-redirector passes a parameter to <b>RxRegisterMinirdr</b> that is a pointer to a large structure, MINIRDR_DISPATCH, which contains configuration information for the network mini-redirector and a dispatch table of pointers to callback routines implemented by the network mini-redirector driver. This configuration data is used to configure internal RDBSS tables for use with this network mini-redirector. RDBSS uses the callback routines passed in this structure to communicate with the network mini-redirector. A network mini-redirector can chose to implement only some of these callback routines. Any callback routine that is not implemented should be set to a <b>NULL</b> pointer in the dispatch table passed to RDBSS. Only callback routines implemented by the network mini-redirector will be called by RDBSS. </p>

<p>Note that the <b>RxRegisterMinirdr</b> routine sets all of the driver dispatch routines of the network mini-redirector driver to point to the top-level RDBSS dispatch routine, <b>RxFsdDispatch</b>. A network mini-redirector can override this behavior by saving a copy of its driver dispatch entry points, calling <b>RxRegisterMinirdr</b>, and rewriting the driver dispatch with its own entry points after the call to <b>RxRegisterMinirdr</b> returns. A network mini-redirector can also prevent its driver dispatch routines from being copied over by the <b>RxRegisterMinirdr</b> routine if the RX_REGISTERMINI_FLAG_DONT_INIT_DRIVER_DISPATCH bit is set in the <i>Controls</i> parameter.</p>

<p>If the <b>RxRegisterMinirdr</b> call is successful, a number of members in RDBSS_DEVICE_OBJECT pointed to by the <i>DeviceObject</i> parameter are initialized including the following: </p>

<p>The <b>Dispatch</b> member is set to the <i>MrdrDispatch</i> parameter.</p>

<p>The <b>RegistrationControls</b> member is set to the <i>Controls</i> parameter.</p>

<p>The <b>DeviceName</b> member is set to the <i>DeviceName</i> parameter.</p>

<p>The <b>RegisterUncProvider</b> member is set to <b>TRUE</b> if the RX_REGISTERMINI_FLAG_DONT_PROVIDE_UNCS bit in the <i>Controls</i> parameter was not set.</p>

<p>The <b>RegisterMailSlotProvider</b> member is set to <b>TRUE</b> if the RX_REGISTERMINI_FLAG_DONT_PROVIDE_MAILSLOTS bit in the <i>Controls</i> parameter was not set.</p>

<p>The <b>NetworkProviderPriority</b> member is set to the network provider priority that MUP will use.</p>

<p>If the <b>RxRegisterMinirdr</b> call is successful and the RX_REGISTERMINI_FLAG_DONT_INIT_PREFIX_N_SCAVENGER bit in the <i>Controls</i> parameter is not set, a number of other members in RDBSS_DEVICE_OBJECT pointed to by the <i>DeviceObject</i> parameter are initialized, including the following: </p>

<p>The <b>pRxNetNameTable</b> member structure is initialized.</p>

<p>The <b>RxNetNameTableInDeviceObject.IsNetNameTable</b> member is set to <b>TRUE</b>.</p>

<p>The <b>pRdbssScavenger</b> member structure is initialized.</p>

<p>If the <b>RxRegisterMinirdr</b> call is successful, RDBSS sets the internal state of the network mini-redirector in RDBSS to RDBSS_STARTABLE.</p>

<p>The network mini-redirector does not actually start operation until it receives a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550829">MRxStart</a> routine, one of the callback routines passed in the MINIRDR_DISPATCH structure. The <b>MrxStart</b> callback routine must be implemented by the network mini-redirector driver if it wishes to receive callbacks for operations, unless the network mini-redirector preserves its own driver dispatch entry points. Otherwise, RDBSS will only allow the following I/O request packets through to the driver until <b>MrxStart</b> returns successfully:</p>

<p>IRP requests for device create operations and device operations where the <i>FileObject-&gt;FileName.Length</i> parameter on the IRPSP is zero and the <i>FileObject-&gt;RelatedFileObject</i> parameter is <b>NULL</b>.</p>

<p>For any other IRP request, the RDBSS dispatch routine, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554468">RxFsdDispatch</a>, will return a status of STATUS_REDIRECTOR_NOT_STARTED. </p>

<p>The RDBSS dispatch routine will also fail any requests for the following I/O request packets:</p>

<p>IRP_MJ_CREATE_MAILSLOT</p>

<p>IRP_MJ_CREATE_NAMED_PIPE</p>

<p>The network mini-redirector <b>MrxStart</b> routine is called by RDBSS when the <b>RxStartMiniRdr</b> routine is called. The RDBSS <b>RxStartMinirdr</b> is usually called as a result of an FSCTL or IOCTL request from a user-mode application or service to start the network mini-redirector. The call to <b>RxStartMinirdr </b>cannot be made from the <b>DriverEntry</b> routine of the network mini-redirector after a successful call to <b>RxRegisterMinirdr </b>because some of the start processing requires that the driver initialization be completed. Once the <b>RxStartMinirdr</b> call is received, RDBSS completes the start process by calling the <b>MrxStart</b> routine of the network mini-redirector. If the call to <b>MrxStart</b> returns success, RDBSS sets the internal state of the mini-redirector in RDBSS to RDBSS_STARTED. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mrx.h (include Mrx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550829">MRxStart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554468">RxFsdDispatch</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554718">RxSetDomainForMailslotBroadcast</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554736">RxStartMinirdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554743">RxStopMinirdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554662">RxpUnregisterMinirdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554744">RxUnregisterMinirdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557374">__RxFillAndInstallFastIoDispatch</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxRegisterMinirdr function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
