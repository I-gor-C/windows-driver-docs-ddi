---
UID: NF.fcb.RxGetFileSizeWithLock
title: RxGetFileSizeWithLock
author: windows-driver-content
description: RxGetFileSizeWithLock gets the file size in the FCB structure using a lock to ensure that the 64-bit value is read consistently.
old-location: ifsk\rxgetfilesizewithlock.htm
ms.assetid: f58c2a7a-0782-47a7-84e6-98df541c875d
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fcb.h
req.include-header: Mrxfcb.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxGetFileSizeWithLock
req.alt-loc: fcb.h
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
ms.keywords: RxGetFileSizeWithLock
req.iface: 
---

# RxGetFileSizeWithLock function



## -description
<p><b>RxGetFileSizeWithLock</b> gets the file size in the FCB structure using a lock to ensure that the 64-bit value is read consistently.</p>


## -syntax

````
VOID RxGetFileSizeWithLock(
  _In_  PFCB      Fcb,
  _Out_ PLONGLONG FileSize
);
````


## -parameters
<dl>

### -param <i>Fcb</i> [in]

<dd>
<p>A pointer to the FCB structure.</p>
</dd>

### -param <i>FileSize</i> [out]

<dd>
<p>A pointer where the file size file will be stored on output.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>RxGetFileSizeWithLock</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when an I/O request packet is received for IRP_MJ_QUERY_INFORMATION, IRP_MJ_SET_INFORMATION, IRP_MJ_READ, or IRP_MJ_WRITE. These IRPs are normally received by RDBSS in response to a user-mode application requesting operations on a file. It is also possible for another kernel driver to issue such an IRP. </p>

<p>These IRPs will normally result in a call to one of the <b>MRxQueryFileInfo, MRxQuerySdInfo</b>, <b>MRxLowIORead</b>, or <b>MRxLowIOWrite</b> routines provided by the network mini-redirector. </p>

<p><b>RxGetFileSizeWithLock</b> acquires a lock on the FCB structure and then reads the file size, and then frees the lock. This lock assures that the file size is protected during this operation, since file size is a 64-bit quantity that requires at least two instructions to read on 32-bit processors. </p>

<p>The <b>RxGetFileSizeWithLock</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when an I/O request packet is received for IRP_MJ_QUERY_INFORMATION, IRP_MJ_SET_INFORMATION, IRP_MJ_READ, or IRP_MJ_WRITE. These IRPs are normally received by RDBSS in response to a user-mode application requesting operations on a file. It is also possible for another kernel driver to issue such an IRP. </p>

<p>These IRPs will normally result in a call to one of the <b>MRxQueryFileInfo, MRxQuerySdInfo</b>, <b>MRxLowIORead</b>, or <b>MRxLowIOWrite</b> routines provided by the network mini-redirector. </p>

<p><b>RxGetFileSizeWithLock</b> acquires a lock on the FCB structure and then reads the file size, and then frees the lock. This lock assures that the file size is protected during this operation, since file size is a 64-bit quantity that requires at least two instructions to read on 32-bit processors. </p>

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
<dt>Fcb.h (include Mrxfcb.h or Fcb.h)</dt>
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
<a href="ifsk.the_fcb_structure">The FCB Structure</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550770">MRxQueryFileInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550776">MRxQuerySdInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxGetFileSizeWithLock function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
