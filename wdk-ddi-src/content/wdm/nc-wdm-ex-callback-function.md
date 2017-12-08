---
UID: NC.wdm.EX_CALLBACK_FUNCTION
title: EX_CALLBACK_FUNCTION
author: windows-driver-content
description: A filter driver's RegistryCallback routine can monitor, block, or modify a registry operation.
old-location: kernel\registrycallback.htm
old-project: kernel
ms.assetid: 220ce3b8-2820-4753-9659-5ce7b4f4f32d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Supported starting with Windows XP (see Return Value section).
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RegistryCallback
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Called at PASSIVE_LEVEL (see Remarks section).
req.iface: 
req.product: Windows 10 or later.
---

# EX_CALLBACK_FUNCTION callback



## -description
<p>A filter driver's <i>RegistryCallback</i> routine can monitor, block, or modify a registry operation.</p>


## -prototype

````
EX_CALLBACK_FUNCTION RegistryCallback;

NTSTATUS RegistryCallback(
  _In_     PVOID CallbackContext,
  _In_opt_ PVOID Argument1,
  _In_opt_ PVOID Argument2
)
{ ... }
````


## -parameters
<dl>

### -param CallbackContext [in]

<dd>
<p>The value that the driver passed as the <i>Context</i> parameter to <a href="..\wdm\nf-wdm-cmregistercallback.md">CmRegisterCallback</a> or <a href="..\wdm\nf-wdm-cmregistercallbackex.md">CmRegisterCallbackEx</a> when it registered this <i>RegistryCallback</i> routine.</p>
</dd>

### -param Argument1 [in, optional]

<dd>
<p>A <a href="kernel.reg_notify_class">REG_NOTIFY_CLASS</a>-typed value that identifies the type of registry operation that is being performed and whether the <i>RegistryCallback</i> routine is being called before or after the registry operation is performed.</p>
</dd>

### -param Argument2 [in, optional]

<dd>
<p>A pointer to a structure that contains information that is specific to the type of registry operation. The structure type depends on the REG_NOTIFY_CLASS-typed value for <i>Argument1</i>, as shown in the following table. For information about which REG_NOTIFY_CLASS-typed values are available for which operating system versions, see <a href="kernel.reg_notify_class">REG_NOTIFY_CLASS</a>.</p>
<table>
<tr>
<th>REG_NOTIFY_CLASS Value</th>
<th>Structure Type</th>
</tr>
<tr>
<td><b>RegNtDeleteKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-delete-key-information.md">REG_DELETE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreDeleteKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-delete-key-information.md">REG_DELETE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostDeleteKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtSetValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-set-value-key-information.md">REG_SET_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreSetValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-set-value-key-information.md">REG_SET_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostSetValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtDeleteValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-delete-value-key-information.md">REG_DELETE_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreDeleteValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-delete-value-key-information.md">REG_DELETE_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostDeleteValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtSetInformationKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-set-information-key-information.md">REG_SET_INFORMATION_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreSetInformationKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-set-information-key-information.md">REG_SET_INFORMATION_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostSetInformationKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtRenameKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-rename-key-information.md">REG_RENAME_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreRenameKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-rename-key-information.md">REG_RENAME_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostRenameKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtEnumerateKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-enumerate-key-information.md">REG_ENUMERATE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreEnumerateKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-enumerate-key-information.md">REG_ENUMERATE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostEnumerateKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtEnumerateValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-enumerate-value-key-information.md">REG_ENUMERATE_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreEnumerateValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-enumerate-value-key-information.md">REG_ENUMERATE_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostEnumerateValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtQueryKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-query-key-information.md">REG_QUERY_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreQueryKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-query-key-information.md">REG_QUERY_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostQueryKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtQueryValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-query-value-key-information.md">REG_QUERY_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreQueryValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-query-value-key-information.md">REG_QUERY_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostQueryValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtQueryMultipleValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-query-multiple-value-key-information.md">REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreQueryMultipleValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-query-multiple-value-key-information.md">REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostQueryMultipleValueKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreCreateKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-pre-create-key-information.md">REG_PRE_CREATE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreCreateKeyEx</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-create-key-information.md">REG_CREATE_KEY_INFORMATION**</a>
</td>
</tr>
<tr>
<td><b>RegNtPostCreateKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-create-key-information.md">REG_POST_CREATE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostCreateKeyEx</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreOpenKey</b></td>
<td>
<a href="kernel.reg_pre_open_key_information">REG_PRE_OPEN_KEY_INFORMATION**</a>
</td>
</tr>
<tr>
<td><b>RegNtPreOpenKeyEx</b></td>
<td>
<a href="kernel.reg_open_key_information">REG_OPEN_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostOpenKey</b></td>
<td>
<a href="kernel.reg_post_open_key_information">REG_POST_OPEN_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostOpenKeyEx</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtKeyHandleClose</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-key-handle-close-information.md">REG_KEY_HANDLE_CLOSE_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreKeyHandleClose</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-key-handle-close-information.md">REG_KEY_HANDLE_CLOSE_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostKeyHandleClose</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreFlushKey</b></td>
<td>
<a href="kernel.reg_flush_key_information">REG_FLUSH_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostFlushKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreLoadKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-load-key-information.md">REG_LOAD_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostLoadKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreUnLoadKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-unload-key-information.md">REG_UNLOAD_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostUnLoadKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreQueryKeySecurity</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-query-key-security-information.md">REG_QUERY_KEY_SECURITY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostQueryKeySecurity</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreSetKeySecurity</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-set-key-security-information.md">REG_SET_KEY_SECURITY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostSetKeySecurity</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtCallbackObjectContextCleanup</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-callback-context-cleanup-information.md">REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreRestoreKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-restore-key-information.md">REG_RESTORE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostRestoreKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-restore-key-information.md">REG_RESTORE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreSaveKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-save-key-information.md">REG_SAVE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostSaveKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-save-key-information.md">REG_SAVE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreReplaceKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-replace-key-information.md">REG_REPLACE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPostReplaceKey</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-replace-key-information.md">REG_REPLACE_KEY_INFORMATION</a>
</td>
</tr>
<tr>
<td><b>RegNtPreQueryKeyName</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-query-key-name.md">REG_QUERY_KEY_NAME</a>
</td>
</tr>
<tr>
<td><b>RegNtPostQueryKeyName</b></td>
<td>
<a href="..\wdm\ns-wdm--reg-post-operation-information.md">REG_POST_OPERATION_INFORMATION</a>
</td>
</tr>
</table>
<p> </p>
<p>** Starting with Windows 7, the actual data structure passed in when the notify class is <b>RegNtPreCreateKeyEx</b> or <b>RegNtPreOpenKeyEx</b> is the V1 version of this structure, <a href="..\wdm\ns-wdm--reg-create-key-information-v1.md">REG_CREATE_KEY_INFORMATION_V1</a> or <a href="kernel.reg_open_key_information_v1">REG_OPEN_KEY_INFORMATION_V1</a>, respectively. Check the <b>Reserved</b> member to determine the version of the structure.</p>
<table>
<tr>
<th>Version number</th>
<th>Structure name</th>
</tr>
<tr>
<td>0</td>
<td><b>REG_CREATE_KEY_INFORMATION</b> and <b>REG_OPEN_KEY_INFORMATION</b></td>
</tr>
<tr>
<td>1</td>
<td><b>REG_CREATE_KEY_INFORMATION_V1</b> and <b>REG_OPEN_KEY_INFORMATION_V1</b></td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p></p><dl>
<dt><a id="_and__"></a><a id="_AND__"></a>Windows XP and Windows Server 2003:</dt>
<dd>
<p>If the <i>RegistryCallback</i> routine returns STATUS_SUCCESS, the configuration manager continues processing the registry operation.</p>
<p>If the <i>RegistryCallback</i> routine returns a status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>FALSE</b>, the configuration manager stops processing the registry operation and returns the specified return value to the calling thread.</p>
</dd>
<dt><a id="_and_later_"></a><a id="_AND_LATER_"></a>Windows Vista and later:</dt>
<dd>
<p>If the <i>RegistryCallback</i> routine returns STATUS_SUCCESS, the configuration manager continues processing the registry operation.</p>
<p>If the <i>RegistryCallback</i> routine returns STATUS_CALLBACK_BYPASS, the configuration manager stops processing the registry operation and returns STATUS_SUCCESS to the calling thread.</p>
<p>If the <i>RegistryCallback</i> routine returns a status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>FALSE</b> (except for STATUS_CALLBACK_BYPASS), the configuration manager stops processing the registry operation and returns the specified return value to the calling thread.</p>
</dd>
</dl><p>If the <i>RegistryCallback</i> routine returns STATUS_SUCCESS, the configuration manager continues processing the registry operation.</p>

<p>If the <i>RegistryCallback</i> routine returns a status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>FALSE</b>, the configuration manager stops processing the registry operation and returns the specified return value to the calling thread.</p>

<p>If the <i>RegistryCallback</i> routine returns STATUS_SUCCESS, the configuration manager continues processing the registry operation.</p>

<p>If the <i>RegistryCallback</i> routine returns STATUS_CALLBACK_BYPASS, the configuration manager stops processing the registry operation and returns STATUS_SUCCESS to the calling thread.</p>

<p>If the <i>RegistryCallback</i> routine returns a status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>FALSE</b> (except for STATUS_CALLBACK_BYPASS), the configuration manager stops processing the registry operation and returns the specified return value to the calling thread.</p>

<p>For more information about when a <i>RegistryCallback</i> routine should return each of these status values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.</p>

## -remarks
<p>To be notified of registry operations, a kernel-mode component (such as the driver component of an antivirus software package) can call <a href="..\wdm\nf-wdm-cmregistercallback.md">CmRegisterCallback</a> or <a href="..\wdm\nf-wdm-cmregistercallbackex.md">CmRegisterCallbackEx</a> to register a <i>RegistryCallback</i> routine.</p>

<p>The <i>RegistryCallback</i> routine can inspect the contents of the input and output buffers that are supplied for registry operations. A registry operation can be initiated by a user-mode application that calls a user-mode registry routine (such as <a href="base.regcreatekeyex">RegCreateKeyEx</a> or <a href="base.regopenkeyex">RegOpenKeyEx</a>) or by a driver that calls a kernel-mode registry routine (such as <a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a> or <a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>). An <i>input buffer</i> is a memory buffer supplied by the initiator from which the registry reads input data for the operation. An <i>output buffer</i> is a buffer supplied by the initiator into which the registry writes output data requested by the initiator.</p>

<p>Before calling the <i>RegistryCallback</i> routine, the kernel probes (to verify alignment and accessibility) all members of the <i>Argument2</i> structures that point to output buffers in user-mode memory, but does not capture user-mode output buffers in system memory. The callback routine must enclose any access of an output buffer in a <b>try</b>/<b>except</b> block. If the callback routine needs to pass an output buffer pointer to a system routine (for example, <a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>), and the buffer is in user-mode memory, the callback routine must first capture the buffer.</p>

<p>The handling of input buffers depends on the Windows version. Starting with Windows 8, the kernel captures all input buffers pointed to by members of the <i>Argument2</i> structures in system memory before calling the <i>RegistryCallback</i> routine. In versions of Windows before Windows 8, the kernel probes all members of the <i>Argument2</i> structures that point to input buffers in user-mode memory, but captures only some of these buffers in system memory. In these earlier versions of Windows, the callback routine must enclose any access of an input buffer in a <b>try</b>/<b>except</b> block. Additionally, if the callback routine needs to pass an input buffer pointer to a system routine (for example, <b>ZwOpenKey</b>), and the buffer is in user-mode memory, the callback routine must first capture the buffer.</p>

<p>The following table summarizes the requirements for buffer accesses by the <i>RegistryCallback</i> routine.</p>

<p>For more information about <i>RegistryCallback</i> routines and registry filter drivers, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.</p>

<p>A <i>RegistryCallback</i> executes at IRQL = PASSIVE_LEVEL and in the context of the thread that is performing the registry operation.</p>

<p>To define a <i>RegistryCallback</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>RegistryCallback</i> callback routine that is named <code>MyRegistryCallback</code>, use the EX_CALLBACK_FUNCTION type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The EX_CALLBACK_FUNCTION function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EX_CALLBACK_FUNCTION function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows XP (see Return Value section).</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at PASSIVE_LEVEL (see Remarks section).</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-cmregistercallback.md">CmRegisterCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-cmunregistercallback.md">CmUnRegisterCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-probeforread.md">ProbeForRead</a>
</dt>
<dt>
<a href="kernel.reg_notify_class">REG_NOTIFY_CLASS</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RegistryCallback routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
