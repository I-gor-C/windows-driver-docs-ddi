---
UID: NF.spbcx.SpbDeviceInitialize
title: SpbDeviceInitialize
author: windows-driver-content
description: The SpbDeviceInitialize method completes the initialization of the SPB controller driver after this driver creates the associated device object.
old-location: spb\spbdeviceinitialize.htm
old-project: SPB
ms.assetid: 2EB57066-164F-445C-8621-7B65E6715E97
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SpbDeviceInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: spbcx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SpbDeviceInitialize
req.alt-loc: spbcxstubs.lib,spbcxstubs.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spbcxstubs.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# SpbDeviceInitialize function



## -description
<p>The <b>SpbDeviceInitialize</b> method completes the initialization of the SPB controller driver after this driver creates the associated device object.</p>


## -syntax

````
NTSTATUS SpbDeviceInitialize(
  _In_ WDFDEVICE              FxDevice,
  _In_ PSPB_CONTROLLER_CONFIG Config
);
````


## -parameters
<dl>

### -param <i>FxDevice</i> [in]

<dd>
<p>A WDFDEVICE handle to the device object that represents the SPB controller.</p>
</dd>

### -param <i>Config</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406206">SPB_CONTROLLER_CONFIG</a> structure that contains the device configuration information for the SPB controller driver.  This structure must have been initialized by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406207">SPB_CONTROLLER_CONFIG_INIT</a> function.</p>
</dd>
</dl>

## -returns
<p><b>SpbDeviceInitialize</b> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns an appropriate NTSTATUS error code.</p>

## -remarks
<p>Your SPB controller driver calls this method to register its event callback functions with the SPB framework extension (SpbCx) and to specify the transfer mode to use for the controller's I/O queue. <b>SpbDeviceInitialize</b> creates all of the controller's internal data structures, including the I/O queue.</p>

<p>The SPB controller driver must call this method before it <i>commits</i> the device object—that is, before it returns from the <i>EvtDriverDeviceAdd</i> callback or adds the PDO to the controller's child list. The child list represents the devices that are attached to the bus. For more information, see <a href="kmdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>After <b>SpbDeviceInitialize</b> returns, the controller is ready to process I/O requests, but the SPB controller driver can, as needed, continue to configure the controller settings before it commits the device object.</p>

<p>If the structure pointed to by <i>Config</i> is not filled out correctly, <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> will raise an error. For more information about the requirements for the <i>Config</i> parameter, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406206">SPB_CONTROLLER_CONFIG</a>.</p>

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
<dt>Spbcx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Spbcxstubs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a>
</dt>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406206">SPB_CONTROLLER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406207">SPB_CONTROLLER_CONFIG_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20SpbDeviceInitialize method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
