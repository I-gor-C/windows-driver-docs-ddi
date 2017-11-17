---
UID: NF.spbcx.SpbControllerSetRequestAttributes
title: SpbControllerSetRequestAttributes
author: windows-driver-content
description: The SpbControllerSetRequestAttributes method sets object attributes that will be used for all SPBREQUEST objects that the SPB framework extension (SpbCx) delivers to the SPB controller driver.
old-location: spb\spbcontrollersetrequestattributes.htm
ms.assetid: 9BE790DB-DB7A-44A3-8A89-673CBFCF4D65
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: SPB
req.header: spbcx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SpbControllerSetRequestAttributes
req.alt-loc: Spbcx.h
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
ms.keywords: SpbControllerSetRequestAttributes
req.iface: 
req.product: Windows 10 or later.
---

# SpbControllerSetRequestAttributes function



## -description
<p>The <b>SpbControllerSetRequestAttributes</b> method  sets object attributes that will be used for all SPBREQUEST objects  that the SPB framework extension (SpbCx) delivers to the SPB controller driver.</p>


## -syntax

````
VOID SpbControllerSetRequestAttributes(
  [in] WDFDEVICE              FxDevice,
  [in] PWDF_OBJECT_ATTRIBUTES RequestAttributes
);
````


## -parameters
<dl>

### -param <i>FxDevice</i> [in]

<dd>
<p>A WDFDEVICE handle to the device object that represents the SPB controller.</p>
</dd>

### -param <i>RequestAttributes</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that contains attributes for the SPB controller's SPBREQUEST objects.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>During device initialization, your SPB controller driver can call this method to set the default attributes for SPBREQUEST objects.  Thereafter, SpbCx assigns these attributes to any I/O requests that it delivers (or forwards) to target devices on the bus.</p>

<p><i>RequestAttributes</i> points to an <b>WDF_OBJECT_ATTRIBUTES</b> structure. The caller must previously have called the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552402">WDF_OBJECT_ATTRIBUTES_INIT</a> function to initialize this structure. After this call, but before the call to <b>SpbControllerSetRequestAttributes</b>, the caller can change the values of the following members of this structure:</p>

<p><b>SpbControllerSetRequestAttributes</b> will use these values as default attributes for SPBREQUEST objects. However, the driver cannot change the default attribute values that are contained in the <b>ExecutionLevel</b>, <b>SynchronizationScope</b>, and <b>ParentObject</b> members.  These members must remain unchanged from the values that the <b>WDF_OBJECT_ATTRIBUTES_INIT</b> function initializes them to.</p>

<p><b>WDF_OBJECT_ATTRIBUTES_INIT</b> initializes the <b>EvtCleanupCallback</b> and <b>EvtDestroyCallback</b> members to <b>NULL</b>. If you change these default values to register an <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> or <a href="https://msdn.microsoft.com/4c3b08d2-bb25-40bd-b2fc-1b9ea2d452b3">EvtDestroyCallback</a> callback function, this function is called each time an I/O request arrives in the SPB controller queue, which is managed by SpbCx. Such an I/O request causes the <i>EvtCleanupCallback</i> or <i>EvtDestroyCallback</i> function to be called even if SpbCx never presents the request to the SPB controller driver (because the request is canceled after it arrives in the queue but before it is passed to the driver).</p>

<p>The SPB controller driver must call <b>SpbControllerSetRequestAttributes</b> before it <i>commits</i> the device object—that is, before it returns from the <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback or adds the PDO to the controller's child list. The child list represents the devices that are attached to the bus. For more information, see <a href="kmdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>During device initialization, your SPB controller driver can call this method to set the default attributes for SPBREQUEST objects.  Thereafter, SpbCx assigns these attributes to any I/O requests that it delivers (or forwards) to target devices on the bus.</p>

<p><i>RequestAttributes</i> points to an <b>WDF_OBJECT_ATTRIBUTES</b> structure. The caller must previously have called the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552402">WDF_OBJECT_ATTRIBUTES_INIT</a> function to initialize this structure. After this call, but before the call to <b>SpbControllerSetRequestAttributes</b>, the caller can change the values of the following members of this structure:</p>

<p><b>SpbControllerSetRequestAttributes</b> will use these values as default attributes for SPBREQUEST objects. However, the driver cannot change the default attribute values that are contained in the <b>ExecutionLevel</b>, <b>SynchronizationScope</b>, and <b>ParentObject</b> members.  These members must remain unchanged from the values that the <b>WDF_OBJECT_ATTRIBUTES_INIT</b> function initializes them to.</p>

<p><b>WDF_OBJECT_ATTRIBUTES_INIT</b> initializes the <b>EvtCleanupCallback</b> and <b>EvtDestroyCallback</b> members to <b>NULL</b>. If you change these default values to register an <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> or <a href="https://msdn.microsoft.com/4c3b08d2-bb25-40bd-b2fc-1b9ea2d452b3">EvtDestroyCallback</a> callback function, this function is called each time an I/O request arrives in the SPB controller queue, which is managed by SpbCx. Such an I/O request causes the <i>EvtCleanupCallback</i> or <i>EvtDestroyCallback</i> function to be called even if SpbCx never presents the request to the SPB controller driver (because the request is canceled after it arrives in the queue but before it is passed to the driver).</p>

<p>The SPB controller driver must call <b>SpbControllerSetRequestAttributes</b> before it <i>commits</i> the device object—that is, before it returns from the <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback or adds the PDO to the controller's child list. The child list represents the devices that are attached to the bus. For more information, see <a href="kmdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

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
<a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552402">WDF_OBJECT_ATTRIBUTES_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20SpbControllerSetRequestAttributes method%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
