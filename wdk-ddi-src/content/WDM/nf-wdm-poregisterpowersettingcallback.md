---
UID: NF.wdm.PoRegisterPowerSettingCallback
title: PoRegisterPowerSettingCallback
author: windows-driver-content
description: The PoRegisterPowerSettingCallback routine registers a power-setting callback routine to receive notifications of changes in the specified power setting.
old-location: kernel\poregisterpowersettingcallback.htm
ms.assetid: a4dd91c4-f6b1-4751-a2be-9b4872fa7bb2
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoRegisterPowerSettingCallback
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: PoRegisterPowerSettingCallback
req.iface: 
req.product: Windows 10 or later.
---

# PoRegisterPowerSettingCallback function



## -description
<p>The <b>PoRegisterPowerSettingCallback</b> routine registers a power-setting callback routine to receive notifications of changes in the specified power setting.</p>


## -syntax

````
NTSTATUS PoRegisterPowerSettingCallback(
  _In_opt_ PDEVICE_OBJECT          DeviceObject,
  _In_     LPCGUID                 SettingGuid,
  _In_     PPOWER_SETTING_CALLBACK Callback,
  _In_opt_ PVOID                   Context,
  _Out_    PVOID                   *Handle
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure that is associated with the caller of this routine. This parameter is optional. It is used internally only for debugging purposes. If this parameter is not supplied, it must be set to <b>NULL</b>.</p>
</dd>

### -param <i>SettingGuid</i> [in]

<dd>
<p>A pointer to the GUID that represents the power setting for this registration. When the specified power setting changes, the power manager calls the callback routine to notify the driver of the change and to supply the new value of the setting. For more information, see Remarks.</p>
</dd>

### -param <i>Callback</i> [in]

<dd>
<p>A pointer to a caller-implemented power-setting callback routine that the power manager calls when the specified power setting changes. For the functional prototype for the callback routine, see <a href="#power_setting_callback">Power-Setting Callback</a>.</p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to the context for the callback routine. This parameter is optional. It is provided so that a driver or device context can be passed to the callback routine. If this parameter is not used, it must be set to <b>NULL</b>.</p>
</dd>

### -param <i>Handle</i> [out]

<dd>
<p>A handle that the power manager uses to represent the callback routine. A driver must subsequently supply this handle in a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff559788">PoUnregisterPowerSettingCallback</a> to unregister the callback routine.</p>
</dd>
</dl>

## -returns
<p><b>PoRegisterPowerSettingCallback</b> returns one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The routine registered the callback routine.</p><dl>
<dt><b>STATUS_ INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The routine could not allocate the system resources that are required to register the callback routine.</p>

<p> </p>

## -remarks
<p>A driver calls <b>PoRegisterPowerSettingCallback</b> to register a callback routine with the power manager. The power manager subsequently calls this callback routine to notify the driver after there is a change to the specified power setting. In addition, the power manager initializes the power setting of the driver by immediately calling the callback routine and passing the current value of the power setting. The power manager initializes the power setting of the driver this way regardless of whether the power setting has actually changed.</p>

<p>A driver should call <b>PoRegisterPowerSettingCallback</b> for each power setting that the driver needs to monitor. Drivers should call this routine in their <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine during initialization. Typically, most drivers pass a pointer to a device extension in the <i>Context</i> parameter.</p>

<p>To unregister a power-setting callback, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559788">PoUnregisterPowerSettingCallback</a> routine.</p>

<p>Typically, Kernel-Mode Driver Framework (KMDF) drivers should call <b>PoRegisterPowerSettingCallback</b> from their <a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a> callback function, and should call <b>PoUnregisterPowerSettingCallback</b> from their <a href="https://msdn.microsoft.com/639ff3fd-ce38-417e-8fc4-a03ad259a5c8">EvtDeviceSelfManagedIoCleanup</a> callback function. These drivers should <u>not</u> call <b>PoRegisterPowerSettingCallback</b> from their <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function; otherwise, the power-setting callback routine might be called before the driver stack is completely built.</p>

<p>The callback routine that is registered for a particular power setting is called when a transition in power state occurs that changes the value of the setting, or when the power manager changes the value of the setting. For example, if <i>SettingGuid</i> points to the GUID value GUID_LIDSWITCH_STATE_CHANGE, the callback routine is called when the lid to a laptop computer clicks open or closed. The <i>Value</i> parameter passed to the callback routine in this example points to a ULONG value that is 1 if the state of the lid switch changed from closed to open, and is 0 if the state of the lid switch changed from open to closed. For more information, see the power-setting GUID definitions and extensive comments in the Wdm.h header file.</p>

<p>The initial call to a callback routine might occur immediately, before the <b>PoRegisterPowerSettingCallback</b> call that registers the routine returns.</p>

<p><b>PoRegisterPowerSettingCallback</b> can be called only at IRQL = PASSIVE_LEVEL.</p>

<p>The function prototype of the power-setting callback routine is as follows:</p>

<p>The power-setting callback parameters are:</p>

<p></p><dl>
<dt><a id="SettingGuid"></a><a id="settingguid"></a><a id="SETTINGGUID"></a><i>SettingGuid</i></dt>
<dd>
<p>A pointer to a GUID that represents the power setting that changed. Power settings and their corresponding GUIDs are defined in Wdm.h.</p>
</dd>
<dt><a id="Value"></a><a id="value"></a><a id="VALUE"></a><i>Value</i></dt>
<dd>
<p>A pointer to the new value of the power setting that changed.</p>
</dd>
<dt><a id="ValueLength"></a><a id="valuelength"></a><a id="VALUELENGTH"></a><i>ValueLength</i></dt>
<dd>
<p>A value of type ULONG that specifies the size, in bytes, of the new power setting value.</p>
</dd>
<dt><a id="Context"></a><a id="context"></a><a id="CONTEXT"></a><i>Context</i></dt>
<dd>
<p>The pointer to the context that a driver supplied in the call to <b>PoRegisterPowerSettingCallback</b> that registered the callback routine.</p>
</dd>
</dl><p>A pointer to a GUID that represents the power setting that changed. Power settings and their corresponding GUIDs are defined in Wdm.h.</p>

<p>A pointer to the new value of the power setting that changed.</p>

<p>A value of type ULONG that specifies the size, in bytes, of the new power setting value.</p>

<p>The pointer to the context that a driver supplied in the call to <b>PoRegisterPowerSettingCallback</b> that registered the callback routine.</p>

<p>The power manager calls a power-setting callback at IRQL = PASSIVE_LEVEL.</p>

<p>To define a power-setting callback routine, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a power-setting callback routine that is named <code>MyPowerSettingCallback</code>, use the POWER_SETTING_CALLBACK type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The POWER_SETTING_CALLBACK function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the POWER_SETTING_CALLBACK function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

<p>A driver calls <b>PoRegisterPowerSettingCallback</b> to register a callback routine with the power manager. The power manager subsequently calls this callback routine to notify the driver after there is a change to the specified power setting. In addition, the power manager initializes the power setting of the driver by immediately calling the callback routine and passing the current value of the power setting. The power manager initializes the power setting of the driver this way regardless of whether the power setting has actually changed.</p>

<p>A driver should call <b>PoRegisterPowerSettingCallback</b> for each power setting that the driver needs to monitor. Drivers should call this routine in their <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine during initialization. Typically, most drivers pass a pointer to a device extension in the <i>Context</i> parameter.</p>

<p>To unregister a power-setting callback, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559788">PoUnregisterPowerSettingCallback</a> routine.</p>

<p>Typically, Kernel-Mode Driver Framework (KMDF) drivers should call <b>PoRegisterPowerSettingCallback</b> from their <a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a> callback function, and should call <b>PoUnregisterPowerSettingCallback</b> from their <a href="https://msdn.microsoft.com/639ff3fd-ce38-417e-8fc4-a03ad259a5c8">EvtDeviceSelfManagedIoCleanup</a> callback function. These drivers should <u>not</u> call <b>PoRegisterPowerSettingCallback</b> from their <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function; otherwise, the power-setting callback routine might be called before the driver stack is completely built.</p>

<p>The callback routine that is registered for a particular power setting is called when a transition in power state occurs that changes the value of the setting, or when the power manager changes the value of the setting. For example, if <i>SettingGuid</i> points to the GUID value GUID_LIDSWITCH_STATE_CHANGE, the callback routine is called when the lid to a laptop computer clicks open or closed. The <i>Value</i> parameter passed to the callback routine in this example points to a ULONG value that is 1 if the state of the lid switch changed from closed to open, and is 0 if the state of the lid switch changed from open to closed. For more information, see the power-setting GUID definitions and extensive comments in the Wdm.h header file.</p>

<p>The initial call to a callback routine might occur immediately, before the <b>PoRegisterPowerSettingCallback</b> call that registers the routine returns.</p>

<p><b>PoRegisterPowerSettingCallback</b> can be called only at IRQL = PASSIVE_LEVEL.</p>

<p>The function prototype of the power-setting callback routine is as follows:</p>

<p>The power-setting callback parameters are:</p>

<p></p><dl>
<dt><a id="SettingGuid"></a><a id="settingguid"></a><a id="SETTINGGUID"></a><i>SettingGuid</i></dt>
<dd>
<p>A pointer to a GUID that represents the power setting that changed. Power settings and their corresponding GUIDs are defined in Wdm.h.</p>
</dd>
<dt><a id="Value"></a><a id="value"></a><a id="VALUE"></a><i>Value</i></dt>
<dd>
<p>A pointer to the new value of the power setting that changed.</p>
</dd>
<dt><a id="ValueLength"></a><a id="valuelength"></a><a id="VALUELENGTH"></a><i>ValueLength</i></dt>
<dd>
<p>A value of type ULONG that specifies the size, in bytes, of the new power setting value.</p>
</dd>
<dt><a id="Context"></a><a id="context"></a><a id="CONTEXT"></a><i>Context</i></dt>
<dd>
<p>The pointer to the context that a driver supplied in the call to <b>PoRegisterPowerSettingCallback</b> that registered the callback routine.</p>
</dd>
</dl><p>A pointer to a GUID that represents the power setting that changed. Power settings and their corresponding GUIDs are defined in Wdm.h.</p>

<p>A pointer to the new value of the power setting that changed.</p>

<p>A value of type ULONG that specifies the size, in bytes, of the new power setting value.</p>

<p>The pointer to the context that a driver supplied in the call to <b>PoRegisterPowerSettingCallback</b> that registered the callback routine.</p>

<p>The power manager calls a power-setting callback at IRQL = PASSIVE_LEVEL.</p>

<p>To define a power-setting callback routine, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a power-setting callback routine that is named <code>MyPowerSettingCallback</code>, use the POWER_SETTING_CALLBACK type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The POWER_SETTING_CALLBACK function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the POWER_SETTING_CALLBACK function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/639ff3fd-ce38-417e-8fc4-a03ad259a5c8">EvtDeviceSelfManagedIoCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559788">PoUnregisterPowerSettingCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoRegisterPowerSettingCallback routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
