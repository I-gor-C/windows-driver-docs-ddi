---
UID: NS.wdm._OB_CALLBACK_REGISTRATION
title: OB_CALLBACK_REGISTRATION
author: windows-driver-content
description: The OB_CALLBACK_REGISTRATION structure specifies the parameters when the ObRegisterCallbacks routine registers ObjectPreCallback and ObjectPostCallback callback routines.
old-location: kernel\ob_callback_registration.htm
old-project: kernel
ms.assetid: e288b050-0875-4c9b-aa72-47845861755a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: OB_CALLBACK_REGISTRATION, OB_CALLBACK_REGISTRATION, *POB_CALLBACK_REGISTRATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Server 2008.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OB_CALLBACK_REGISTRATION
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
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# OB_CALLBACK_REGISTRATION structure



## -description
<p>The <b>OB_CALLBACK_REGISTRATION</b> structure specifies the parameters when the <a href="..\wdm\nf-wdm-obregistercallbacks.md">ObRegisterCallbacks</a> routine registers <a href="kernel.objectprecallback">ObjectPreCallback</a> and <a href="kernel.objectpostcallback">ObjectPostCallback</a> callback routines.</p>


## -syntax

````
typedef struct _OB_CALLBACK_REGISTRATION {
  USHORT                    Version;
  USHORT                    OperationRegistrationCount;
  UNICODE_STRING            Altitude;
  PVOID                     RegistrationContext;
  OB_OPERATION_REGISTRATION *OperationRegistration;
} OB_CALLBACK_REGISTRATION, *POB_CALLBACK_REGISTRATION;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of object callback registration that is requested. Drivers should specify OB_FLT_REGISTRATION_VERSION.</p>
</dd>

### -field <b>OperationRegistrationCount</b>

<dd>
<p>The number of entries in the <b>OperationRegistration</b> array.</p>
</dd>

### -field <b>Altitude</b>

<dd>
<p>A Unicode string that specifies the altitude of the driver. For more information about altitude, see <a href="ifsk.load_order_groups_and_altitudes_for_minifilter_drivers">Load Order Groups and Altitudes for Minifilter Drivers</a>.</p>
</dd>

### -field <b>RegistrationContext</b>

<dd>
<p>The system passes the <b>RegistrationContext</b> value to the callback routine when the callback routine is run. The meaning of this value is driver-defined.</p>
</dd>

### -field <b>OperationRegistration</b>

<dd>
<p>A pointer to an array of <a href="..\wdm\ns-wdm--ob-operation-registration.md">OB_OPERATION_REGISTRATION</a> structures. Each structure specifies <a href="kernel.objectprecallback">ObjectPreCallback</a> and <a href="kernel.objectpostcallback">ObjectPostCallback</a> callback routines and the types of operations that the routines are called for. </p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="..\wdm\nf-wdm-obregistercallbacks.md">ObRegisterCallbacks</a> routine. The <i>CallBackRegistration</i> parameter to this routine is a pointer to a buffer that contains an <b>OB_CALLBACK_REGISTRATION</b> structure that is followed by an array of one or more <a href="..\wdm\ns-wdm--ob-operation-registration.md">OB_OPERATION_REGISTRATION</a> structures.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Server 2008.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--ob-operation-registration.md">OB_OPERATION_REGISTRATION</a>
</dt>
<dt>
<a href="kernel.objectpostcallback">ObjectPostCallback</a>
</dt>
<dt>
<a href="kernel.objectprecallback">ObjectPreCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obregistercallbacks.md">ObRegisterCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20OB_CALLBACK_REGISTRATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
