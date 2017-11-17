---
UID: NF.fcb.RxpDereferenceNetFcb
title: RxpDereferenceNetFcb
author: windows-driver-content
description: RxpDereferenceNetFcb decrements the reference count on an FCB structure.
old-location: ifsk\rxpdereferencenetfcb.htm
ms.assetid: 6e59a1c7-ddd4-40a6-8e75-879cbef010db
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fcb.h
req.include-header: Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxpDereferenceNetFcb
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
ms.keywords: RxpDereferenceNetFcb
req.iface: 
---

# RxpDereferenceNetFcb function



## -description
<p><b>RxpDereferenceNetFcb</b> decrements the reference count on an FCB structure.</p>


## -syntax

````
LONG RxpDereferenceNetFcb(
   PFCB Fcb
);
````


## -parameters
<dl>

### -param <i>Fcb</i> 

<dd>
<p>A pointer to the FCB structure to be dereferenced.</p>
</dd>
</dl>

## -returns
<p><b>RxpDereferenceNetFcb</b> returns the final reference count after the dereference. </p>

## -remarks
<p>The referencing and dereferencing of FCBs is different from those of the other data structures because of the embedded resource in the FCB. This implies that the caller requires information regarding the status of the FCB (whether it was finalized or not ). To finalize the FCB, two locks need to be held, the NET_ROOT name table lock as well as the FCB resource. These considerations lead to a different approach in dereferencing FCBs. Consequently, <b>RxpDereferenceNetFcb</b> does not attempt to finalize the FCB.</p>

<p>A number of macros are defined in <i>fcb.h</i> for debugging that are the preferred way to call this routine. These macros provide a wrapper around the <b>RxpReferenceNetFcb</b>  or <b>RxpDereferenceNetFcb</b> routines used for file structure management operations on FCB structures. The <b>RxDereferenceNetFcb</b> macro is the preferred way to call this routine. This macro first calls the <b>RxpTrackDereference</b> routine to log diagnostic information about the request before calling the <b>RxpDereferenceNetFcb</b> routine.</p>

<p>On checked builds, <b>RxpDereferenceNetFcb</b> causes the system to ASSERT if the node type for the structure is not an FCB or if the final reference count is less than 0. </p>

<p>The referencing and dereferencing of FCBs is different from those of the other data structures because of the embedded resource in the FCB. This implies that the caller requires information regarding the status of the FCB (whether it was finalized or not ). To finalize the FCB, two locks need to be held, the NET_ROOT name table lock as well as the FCB resource. These considerations lead to a different approach in dereferencing FCBs. Consequently, <b>RxpDereferenceNetFcb</b> does not attempt to finalize the FCB.</p>

<p>A number of macros are defined in <i>fcb.h</i> for debugging that are the preferred way to call this routine. These macros provide a wrapper around the <b>RxpReferenceNetFcb</b>  or <b>RxpDereferenceNetFcb</b> routines used for file structure management operations on FCB structures. The <b>RxDereferenceNetFcb</b> macro is the preferred way to call this routine. This macro first calls the <b>RxpTrackDereference</b> routine to log diagnostic information about the request before calling the <b>RxpDereferenceNetFcb</b> routine.</p>

<p>On checked builds, <b>RxpDereferenceNetFcb</b> causes the system to ASSERT if the node type for the structure is not an FCB or if the final reference count is less than 0. </p>

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
<dt>Fcb.h (include Fcb.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554627">RxpReferenceNetFcb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554655">RxpTrackDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554659">RxpTrackReference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxpDereferenceNetFcb function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
