---
UID: NS.fltkernel._FLT_REGISTRATION
title: FLT_REGISTRATION
author: windows-driver-content
description: The FLT_REGISTRATION structure is passed as a parameter to FltRegisterFilter.
old-location: ifsk\flt_registration.htm
old-project: ifsk
ms.assetid: 3313af42-0e0a-4ad0-b0bb-0afb795e24fd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FLT_REGISTRATION, FLT_REGISTRATION, *PFLT_REGISTRATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FLT_REGISTRATION
req.alt-loc: fltkernel.h
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

# FLT_REGISTRATION structure



## -description
<p>The FLT_REGISTRATION structure is passed as a parameter to <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>. </p>


## -syntax

````
typedef struct _FLT_REGISTRATION {
  USHORT                                      Size;
  USHORT                                      Version;
  FLT_REGISTRATION_FLAGS                      Flags;
  const FLT_CONTEXT_REGISTRATION              *ContextRegistration;
  const FLT_OPERATION_REGISTRATION            *OperationRegistration;
  PFLT_FILTER_UNLOAD_CALLBACK                 FilterUnloadCallback;
  PFLT_INSTANCE_SETUP_CALLBACK                InstanceSetupCallback;
  PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK       InstanceQueryTeardownCallback;
  PFLT_INSTANCE_TEARDOWN_CALLBACK             InstanceTeardownStartCallback;
  PFLT_INSTANCE_TEARDOWN_CALLBACK             InstanceTeardownCompleteCallback;
  PFLT_GENERATE_FILE_NAME                     GenerateFileNameCallback;
  PFLT_NORMALIZE_NAME_COMPONENT               NormalizeNameComponentCallback;
  PFLT_NORMALIZE_CONTEXT_CLEANUP              NormalizeContextCleanupCallback;
#if FLT_MGR_LONGHORN
  PFLT_TRANSACTION_NOTIFICATION_CALLBACK      TransactionNotificationCallback;
  PFLT_NORMALIZE_NAME_COMPONENT_EX            NormalizeNameComponentExCallback;
#endif 
#ifdef FLT_MFG_WIN8
  PFLT_SECTION_CONFLICT_NOTIFICATION_CALLBACK SectionNotificationCallback;
#endif 
} FLT_REGISTRATION, *PFLT_REGISTRATION;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of the FLT_REGISTRATION structure. Minifilter drivers must set this member to <b>sizeof</b>(FLT_REGISTRATION). </p>
</dd>

### -field <b>Version</b>

<dd>
<p>The revision level of the FLT_REGISTRATION structure. Minifilter drivers must set this member to FLT_REGISTRATION_VERSION. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitmask of minifilter registration flags. This member can be <b>NULL</b> or a combination of the following. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="FLTFL_REGISTRATION_DO_NOT_SUPPORT_SERVICE_STOP"></a><a id="fltfl_registration_do_not_support_service_stop"></a><dl>

### -field <b>FLTFL_REGISTRATION_DO_NOT_SUPPORT_SERVICE_STOP</b>

</dl>
</td>
<td width="60%">
<p>If this flag is set, the minifilter is not unloaded in response to service stop requests, even if the <b>FilterUnloadCallback</b> member is not <b>NULL</b>. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FLTFL_REGISTRATION_SUPPORT_NPFS_MSFS"></a><a id="fltfl_registration_support_npfs_msfs"></a><dl>

### -field <b>FLTFL_REGISTRATION_SUPPORT_NPFS_MSFS</b>

</dl>
</td>
<td width="60%">
<p>If this flag is set,  the minifilter will support filtering of named pipe and mailslot requests.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="FLTFL_REGISTRATION_SUPPORT_DAX_VOLUME"></a><a id="fltfl_registration_support_dax_volume"></a><dl>

### -field <b>FLTFL_REGISTRATION_SUPPORT_DAX_VOLUME</b>

</dl>
</td>
<td width="60%">
<p>If this flag is set, the minifilter will support attaching to a direct access (DAX) volume. This will indicate to Filter Manager that the minifilter will filter the DAX volume. This flag was introduced in Windows 10, version 1607.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ContextRegistration</b>

<dd>
<p> A variable-length array of <a href="..\fltkernel\ns-fltkernel--flt-context-registration.md">FLT_CONTEXT_REGISTRATION</a> structures, one for each context type that the minifilter uses. The last element in the array must be {FLT_CONTEXT_END}. </p>
</dd>

### -field <b>OperationRegistration</b>

<dd>
<p>A variable-length array of <a href="..\fltkernel\ns-fltkernel--flt-operation-registration.md">FLT_OPERATION_REGISTRATION</a> structures, one for each type of I/O for which the minifilter registers preoperation (<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>) and postoperation (<a href="..\fltkernel\nc-fltkernel-pflt-post-operation-callback.md">PFLT_POST_OPERATION_CALLBACK</a>) callback routines. The last element in the array must be {IRP_MJ_OPERATION_END}. </p>
</dd>

### -field <b>FilterUnloadCallback</b>

<dd>
<p>A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-filter-unload-callback.md">PFLT_FILTER_UNLOAD_CALLBACK</a> to be registered as the minifilter's <i>FilterUnloadCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>InstanceSetupCallback</b>

<dd>
<p>A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-instance-setup-callback.md">PFLT_INSTANCE_SETUP_CALLBACK</a> to be registered as the minifilter's <i>InstanceSetupCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>InstanceQueryTeardownCallback</b>

<dd>
<p>A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-instance-query-teardown-callback.md">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a> to be registered as the minifilter's <i>InstanceQueryTeardownCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>InstanceTeardownStartCallback</b>

<dd>
<p>A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md">PFLT_INSTANCE_TEARDOWN_CALLBACK</a> to be registered as the minifilter's <i>InstanceTeardownStartCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>InstanceTeardownCompleteCallback</b>

<dd>
<p>A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md">PFLT_INSTANCE_TEARDOWN_CALLBACK</a> to be registered as the minifilter's <i>InstanceTeardownCompleteCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>GenerateFileNameCallback</b>

<dd>
<p>A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-generate-file-name.md">PFLT_GENERATE_FILE_NAME</a> to be registered as the minifilter's <i>GenerateFileNameCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>NormalizeNameComponentCallback</b>

<dd>
<p>A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-normalize-name-component.md">PFLT_NORMALIZE_NAME_COMPONENT</a> to be registered as the minifilter's <i>NormalizeNameComponentCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>NormalizeContextCleanupCallback</b>

<dd>
<p>A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-normalize-context-cleanup.md">PFLT_NORMALIZE_CONTEXT_CLEANUP</a> to be registered as the minifilter's <i>NormalizeContextCleanupCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>TransactionNotificationCallback</b>

<dd>
<p>(Windows Vista and later only.)  A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-transaction-notification-callback.md">PFLT_TRANSACTION_NOTIFICATION_CALLBACK</a> to be registered as the minifilter's <i>TransactionNotificationCallback</i> routine. This member is optional and can be <b>NULL</b>. </p>
</dd>

### -field <b>NormalizeNameComponentExCallback</b>

<dd>
<p>(Windows Vista and later only.)   A pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-normalize-name-component-ex.md">PFLT_NORMALIZE_NAME_COMPONENT_EX</a> to be registered as the minifilter driver's <i>NormalizeNameComponentExCallback</i> routine. This member is optional and can be <b>NULL</b>.  </p>
<p>Compared to the <i>NormalizeNameComponentCallback</i> callback routine, the <i>NormalizeNameComponentExCallback</i> callback routine supports an additional file object parameter,   <i> FileObject</i> (of type PFILE_OBJECT). A minifilter driver can use this parameter to acquire additional information, such as that provided by the <a href="..\ntddk\ns-ntddk--txn-parameter-block.md">TXN_PARAMETER_BLOCK</a> structure.</p>
<p>A minifilter driver can simultaneously set both the <i>NormalizeNameComponentCallback</i> and <i>NormalizeNameComponentExCallback</i> members to <b>NULL</b>; however, a name provider minifilter driver must register either a <i>NormalizeNameComponentCallback</i> or <i>NormalizeNameComponentExCallback</i> callback routine, or both.  For example, a name provider minifilter driver that has no use for the additional <i>FileObject</i> parameter can set the <i>NormalizeNameComponentExCallback</i> member to <b>NULL</b> and only provide a <i>NormalizeNameComponentCallback</i> callback routine.</p>
<p>A minifilter driver can provide both a <i>NormalizeNameComponentCallback</i> callback and a <i>NormalizeNameComponentExCallback</i> callback.  In this case, starting with Windows Vista, the filter manager will use only the <i>NormalizeNameComponentExCallback</i> callback; for Windows operating systems prior to Windows Vista, the filter manager will  use only the <i>NormalizeNameComponentCallback</i> callback. This allows the same minifilter driver binary to run under all versions of the operating system.</p>
</dd>

### -field <b>SectionNotificationCallback</b>

<dd>
<p>Pointer to a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-section-conflict-notification-callback.md">PFLT_SECTION_CONFLICT_NOTIFICATION_CALLBACK</a> to be registered as the minifilter's <i>SectionNotificationCallback</i> routine. This member is optional and can be <b>NULL</b>. This callback is called for notifications of I/O failures for sections created with <a href="..\fltkernel\nf-fltkernel-fltcreatesectionfordatascan.md">FltCreateSectionForDatascan</a>.</p>
</dd>
</dl>

## -remarks
<p>The FLT_REGISTRATION structure is used to provide information about a file system minifilter, such as a <i>FilterUnloadCallback</i> (<a href="..\fltkernel\nc-fltkernel-pflt-filter-unload-callback.md">PFLT_FILTER_UNLOAD_CALLBACK</a>) routine and preoperation (<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>) and postoperation (<a href="..\fltkernel\nc-fltkernel-pflt-post-operation-callback.md">PFLT_POST_OPERATION_CALLBACK</a>) callback routines, to the filter manager. The minifilter passes a pointer to this structure as the <i>Registration</i> parameter to <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-context-registration.md">FLT_CONTEXT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-operation-registration.md">FLT_OPERATION_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-filter-unload-callback.md">PFLT_FILTER_UNLOAD_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-generate-file-name.md">PFLT_GENERATE_FILE_NAME</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-query-teardown-callback.md">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-setup-callback.md">PFLT_INSTANCE_SETUP_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-normalize-context-cleanup.md">PFLT_NORMALIZE_CONTEXT_CLEANUP</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-normalize-name-component.md">PFLT_NORMALIZE_NAME_COMPONENT</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-normalize-name-component-ex.md">PFLT_NORMALIZE_NAME_COMPONENT_EX</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-post-operation-callback.md">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-transaction-notification-callback.md">PFLT_TRANSACTION_NOTIFICATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_REGISTRATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
