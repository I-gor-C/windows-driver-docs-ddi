---
UID: NF.fltkernel.FltGetUpperInstance
title: FltGetUpperInstance
author: windows-driver-content
description: The FltGetUpperInstance routine returns an opaque instance pointer for the next higher minifilter driver instance, if there is one, that is attached above a given minifilter driver instance on the same volume.
old-location: ifsk\fltgetupperinstance.htm
old-project: ifsk
ms.assetid: 01e7760c-b10c-497e-9cab-4d839c2ce5ff
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltGetUpperInstance
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetUpperInstance
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltGetUpperInstance function



## -description
<p>The <b>FltGetUpperInstance</b> routine returns an opaque instance pointer for the next higher minifilter driver instance, if there is one, that is attached above a given minifilter driver instance on the same volume. </p>


## -syntax

````
NTSTATUS FltGetUpperInstance(
  _In_  PFLT_INSTANCE CurrentInstance,
  _Out_ PFLT_INSTANCE *UpperInstance
);
````


## -parameters
<dl>

### -param <i>CurrentInstance</i> [in]

<dd>
<p>Opaque instance pointer for the instance for which the next higher instance is requested. </p>
</dd>

### -param <i>UpperInstance</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives an opaque instance pointer for the next higher instance. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltGetUpperInstance</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: </p><dl>
<dt><b>STATUS_NO_MORE_ENTRIES</b></dt>
</dl><p>No higher instance was found. This is a warning code. </p>

<p> </p>

## -remarks
<p>One instance is said to be <i>above</i> another if it is attached at a higher altitude on the same volume. The term "altitude" refers to the position that an instance occupies (or should occupy) in the minifilter driver instance stack for a volume. The higher the altitude, the farther the instance is from the base file system in the stack. Only one instance can be attached at a given altitude on a given volume. </p>

<p>Altitude is specified by an <i>altitude string</i>, which is a counted Unicode string consisting of one or more decimal digits in the range of 0 through 9, and it can include a single decimal point. For example, "100.123456" and "03333" are valid altitude strings. </p>

<p>The string "03333" represents a higher altitude than "100.123456". (Leading and trailing zeros are ignored.) In other words, an instance whose altitude is "03333" is farther from the base file system than an instance whose altitude is "100.123456". However, this comparison is only meaningful if both instances are attached to the same volume. </p>

<p><b>FltGetUpperInstance</b> adds a rundown reference to the opaque instance pointer returned in the <i>UpperInstance</i> parameter. When this pointer is no longer needed, the caller must release it by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a>. Thus every successful call to <b>FltGetUpperInstance</b> must be matched by a subsequent call to <b>FltObjectDereference</b>. </p>

<p>One instance is said to be <i>above</i> another if it is attached at a higher altitude on the same volume. The term "altitude" refers to the position that an instance occupies (or should occupy) in the minifilter driver instance stack for a volume. The higher the altitude, the farther the instance is from the base file system in the stack. Only one instance can be attached at a given altitude on a given volume. </p>

<p>Altitude is specified by an <i>altitude string</i>, which is a counted Unicode string consisting of one or more decimal digits in the range of 0 through 9, and it can include a single decimal point. For example, "100.123456" and "03333" are valid altitude strings. </p>

<p>The string "03333" represents a higher altitude than "100.123456". (Leading and trailing zeros are ignored.) In other words, an instance whose altitude is "03333" is farther from the base file system than an instance whose altitude is "100.123456". However, this comparison is only meaningful if both instances are attached to the same volume. </p>

<p><b>FltGetUpperInstance</b> adds a rundown reference to the opaque instance pointer returned in the <i>UpperInstance</i> parameter. When this pointer is no longer needed, the caller must release it by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a>. Thus every successful call to <b>FltGetUpperInstance</b> must be matched by a subsequent call to <b>FltObjectDereference</b>. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541772">FltAttachVolume</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541775">FltAttachVolumeAtAltitude</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541889">FltCompareInstanceAltitudes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542995">FltGetBottomInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543090">FltGetLowerInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543170">FltGetTopInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetUpperInstance routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
