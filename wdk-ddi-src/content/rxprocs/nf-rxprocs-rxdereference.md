---
UID: NF.rxprocs.RxDereference
title: RxDereference
author: windows-driver-content
description: RxDereference decrements the NodeReferenceCount member of a structure by one for several reference counted data structures used by RDBSS.
old-location: ifsk\rxdereference.htm
old-project: ifsk
ms.assetid: 4f63fc92-56e3-4414-a912-09ed0de59c92
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxDereference
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxprocs.h
req.include-header: Rxprocs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxDereference
req.alt-loc: rxprocs.h
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
req.product: Windows 10 or later.
---

# RxDereference function



## -description
<p><b>RxDereference</b> decrements the <b>NodeReferenceCount</b> member of a structure by one for several reference counted data structures used by RDBSS. </p>


## -syntax

````
VOID RxDereference(
  _Inout_ PVOID              Instance,
  _In_    LOCK_HOLDING_STATE LockHoldingState
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in, out]

<dd>
<p>A pointer to the reference-counted data structure to be dereferenced. </p>
</dd>

### -param <i>LockHoldingState</i> [in]

<dd>
<p>The mode in which the appropriate lock for this data structure is held. This parameter can be one of the following values for the LOCK_HOLDING_STATE enumeration:</p>
<p></p>
<dl>

### -param <a id="LHS_LockNotHeld"></a><a id="lhs_locknotheld"></a><a id="LHS_LOCKNOTHELD"></a>LHS_LockNotHeld

<dd>
<p>A lock is not currently held.</p>
</dd>

### -param <a id="LHS_SharedLockHeld"></a><a id="lhs_sharedlockheld"></a><a id="LHS_SHAREDLOCKHELD"></a>LHS_SharedLockHeld

<dd>
<p>A shared lock is being held.</p>
</dd>

### -param <a id="LHS_ExclusiveLockHeld"></a><a id="lhs_exclusivelockheld"></a><a id="LHS_EXCLUSIVELOCKHELD"></a>LHS_ExclusiveLockHeld

<dd>
<p>An exclusive lock is being held.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p><b>RxDereference</b> can be used to dereference (decrement by one) the <b>NodeReferenceCount</b> member on the following data structures used by RDBSS:</p><dl>
<dd>
<p>SRV_CALL</p>
</dd>
<dd>
<p>NET_ROOT</p>
</dd>
<dd>
<p>V_NET_ROOT</p>
</dd>
<dd>
<p>SRV_OPEN</p>
</dd>
<dd>
<p>FOBX</p>
</dd>
</dl><p>SRV_CALL</p>

<p>NET_ROOT</p>

<p>V_NET_ROOT</p>

<p>SRV_OPEN</p>

<p>FOBX</p>

<p>If <b>RxDereference</b> is called with any other type of RDBSS data structure, the routine causes the system to ASSERT on checked builds.</p>

<p>If the <b>NodeReferenceCount</b> member is less than 0 after being derefenced (decremented) by <b>RxDereference</b>, then <b>RxDereference</b> causes the system to ASSERT on checked builds. </p>

<p>If the <b>NodeReferenceCount</b> member decrements to 1 and the <i>LockHoldingState</i> parameter was LHS_ExclusiveLockHeld, the instance of the data structure can be finalized immediately. Otherwise, the instance of the data structure is tagged to be scavenged and finalized later. </p>

<p><b>RxDereference</b> can be used to dereference (decrement by one) the <b>NodeReferenceCount</b> member on the following data structures used by RDBSS:</p><dl>
<dd>
<p>SRV_CALL</p>
</dd>
<dd>
<p>NET_ROOT</p>
</dd>
<dd>
<p>V_NET_ROOT</p>
</dd>
<dd>
<p>SRV_OPEN</p>
</dd>
<dd>
<p>FOBX</p>
</dd>
</dl><p>SRV_CALL</p>

<p>NET_ROOT</p>

<p>V_NET_ROOT</p>

<p>SRV_OPEN</p>

<p>FOBX</p>

<p>If <b>RxDereference</b> is called with any other type of RDBSS data structure, the routine causes the system to ASSERT on checked builds.</p>

<p>If the <b>NodeReferenceCount</b> member is less than 0 after being derefenced (decremented) by <b>RxDereference</b>, then <b>RxDereference</b> causes the system to ASSERT on checked builds. </p>

<p>If the <b>NodeReferenceCount</b> member decrements to 1 and the <i>LockHoldingState</i> parameter was LHS_ExclusiveLockHeld, the instance of the data structure can be finalized immediately. Otherwise, the instance of the data structure is tagged to be scavenged and finalized later. </p>

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
<dt>Rxprocs.h (include Rxprocs.h)</dt>
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
<a href="ifsk.the_fobx_structure">The FOBX Structure</a>
</dt>
<dt>
<a href="ifsk.the_net_root_structure">The NET_ROOT Structure</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554688">RxReference</a>
</dt>
<dt>
<a href="ifsk.the_srv_call_structure">The SRV_CALL Structure</a>
</dt>
<dt>
<a href="ifsk.the_srv_open_structure">The SRV_OPEN Structure</a>
</dt>
<dt>
<a href="ifsk.the_v_net_root_structure">The V_NET_ROOT Structure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxDereference function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
