---
UID: NF.wdm.NtEnumerateTransactionObject
title: NtEnumerateTransactionObject
author: windows-driver-content
description: The ZwEnumerateTransactionObject routine enumerates the KTM objects on a computer.
old-location: kernel\zwenumeratetransactionobject.htm
old-project: kernel
ms.assetid: 49560022-a690-4259-b725-f8927af31804
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NtEnumerateTransactionObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later operating system versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwEnumerateTransactionObject,NtEnumerateTransactionObject
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# NtEnumerateTransactionObject function



## -description
<p>The <b>ZwEnumerateTransactionObject</b> routine enumerates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554272">KTM objects</a> on a computer.</p>


## -syntax

````
NTSTATUS ZwEnumerateTransactionObject(
  _In_opt_ HANDLE            RootObjectHandle,
  _In_     KTMOBJECT_TYPE    QueryType,
  _Inout_  PKTMOBJECT_CURSOR ObjectCursor,
  _In_     ULONG             ObjectCursorLength,
  _Out_    PULONG            ReturnLength
);
````


## -parameters
<dl>

### -param RootObjectHandle [in, optional]

<dd>
<p>A handle to a KTM object. The routine enumerates the child objects of the specified object. This parameter is optional and can be <b>NULL</b>. For more information about valid values for this parameter, see the table in the following Remarks section.</p>
</dd>

### -param QueryType [in]

<dd>
<p>A <a href="..\wdm\ne-wdm--ktmobject-type.md">KTMOBJECT_TYPE</a>-typed value that identifies the object type to enumerate. For more information about valid values for this parameter, see the table in the following Remarks section.</p>
</dd>

### -param ObjectCursor [in, out]

<dd>
<p>A pointer to a caller-allocated buffer that begins with a <a href="..\wdm\ns-wdm--ktmobject-cursor.md">KTMOBJECT_CURSOR</a> structure. <b>ZwEnumerateTransactionObject</b> uses the buffer to store the GUIDs of objects that it finds.</p>
</dd>

### -param ObjectCursorLength [in]

<dd>
<p>The length, in bytes, of the buffer that <i>ObjectCursor</i> points to.</p>
</dd>

### -param ReturnLength [out]

<dd>
<p>A pointer to a caller-allocated location that receives the number of bytes that <b>ZwEnumerateTransactionObject</b> returns in the <i>ObjectCursor</i> buffer, including the length of the <b>KTMOBJECT_CURSOR</b> structure and the length of all returned GUIDs.</p>
</dd>
</dl>

## -returns
<p><b>ZwEnumerateTransactionObject</b> returns STATUS_SUCCESS if the operation succeeds but the routine has not enumerated all the objects. If there are no more objects to enumerate, the routine returns STATUS_NO_MORE_ENTRIES. Otherwise, this routine might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>QueryType</i> or <i>ObjectCursorLength</i> parameter's value is invalid.</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The handle that the <i>RootObjectHandle</i> parameter specifies is not a handle to a valid KTM object.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>An object handle is invalid.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller does not have appropriate access to the objects that are being enumerated.</p>

<p> </p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>The following table contains the valid values for the <i>RootObjectHandle</i> and <i>QueryType</i> parameters.</p>

<p>KTMOBJECT_TRANSACTION_MANAGER</p>

<p><b>NULL</b></p>

<p>All transaction manager objects</p>

<p>KTMOBJECT_RESOURCE_MANAGER</p>

<p>A handle to a transaction manager object.</p>

<p>The handle must have TRANSACTIONMANAGER_QUERY_INFORMATION access to the object.</p>

<p>All resource manager objects that belong to the specified transaction manager object</p>

<p>KTMOBJECT_ENLISTMENT</p>

<p>A handle to a resource manager object.</p>

<p>The handle must have RESOURCEMANAGER_QUERY_INFORMATION access to the object.</p>

<p>All enlistment objects that belong to the specified resource manager object</p>

<p>KTMOBJECT_TRANSACTION</p>

<p>All transaction objects that belong to the specified transaction manager object</p>

<p>All transaction objects that belong to all transaction manager objects</p>

<p>Most TPS components do not have to call <b>ZwEnumerateTransactionObject</b>, but the routine might be useful if you have to write a debugging utility.</p>

<p>Before your component calls <b>ZwEnumerateTransactionObject</b>, it must allocate and zero the buffer that <i>ObjectCursor</i> points to. The buffer's GUID array can be large enough to receive one or more elements. </p>

<p>To enumerate all of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554272">KTM objects</a> of the specified type, your component must call <b>ZwEnumerateTransactionObject</b> repeatedly until it returns STATUS_NO_MORE_ENTRIES. </p>

<p>Every time that the routine is called, it fills the buffer's GUID array with as many object GUIDs that will fit. After each call, your component can use the <a href="..\wdm\ns-wdm--ktmobject-cursor.md">KTMOBJECT_CURSOR</a> structure's <b>ObjectIdCount</b> member to determine the number of object GUIDs that the routine stored in the array.</p>

<p><b>NtEnumerateTransactionObject</b> and <b>ZwEnumerateTransactionObject</b> are two versions of the same Windows Native System Services routine.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>The following code example shows how to enumerate all of the transaction objects on a computer. In this example, the <b>KTMOBJECT_CURSOR</b> structure's GUID array contains only one element, so each call to <b>ZwEnumerateTransactionObject</b> returns one GUID. The routine creates a Unicode string from the GUID and displays the string.</p>

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
<p>Available in Windows Vista and later operating system versions.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--ktmobject-cursor.md">KTMOBJECT_CURSOR</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--ktmobject-type.md">KTMOBJECT_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwEnumerateTransactionObject routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
