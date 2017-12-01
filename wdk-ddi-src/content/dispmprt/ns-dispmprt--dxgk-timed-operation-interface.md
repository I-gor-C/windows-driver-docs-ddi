---
UID: NS.dispmprt._DXGK_TIMED_OPERATION_INTERFACE
title: DXGK_TIMED_OPERATION_INTERFACE
author: windows-driver-content
description: The DXGK_TIMED_OPERATION_INTERFACE structure contains pointers to functions in the Timed Operation Interface, which is implemented by the display port driver.
old-location: display\dxgk_timed_operation_interface.htm
old-project: display
ms.assetid: 85b3764d-00b5-4e1d-bedc-c59a6b182735
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_TIMED_OPERATION_INTERFACE, DXGK_TIMED_OPERATION_INTERFACE, *PDXGK_TIMED_OPERATION_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_TIMED_OPERATION_INTERFACE
req.alt-loc: dispmprt.h
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

# DXGK_TIMED_OPERATION_INTERFACE structure



## -description
<p>The DXGK_TIMED_OPERATION_INTERFACE structure contains pointers to functions in the <a href="display.timed_operation_interface">Timed Operation Interface</a>, which is implemented by the display port driver.</p>


## -syntax

````
typedef struct _DXGK_TIMED_OPERATION_INTERFACE {
  USHORT                 Size;
  USHORT                 Version;
  PVOID                  Context;
  PINTERFACE_REFERENCE   InterfaceReference;
  PINTERFACE_DEREFERENCE InterfaceDereference;
  NTSTATUS               (*TimedOperationStart)(
      _Out_ DXGK_TIMED_OPERATION *Op, 
      _In_ const LARGE_INTEGER *Timeout, 
      _In_ BOOLEAN OsHandled);
  NTSTATUS               (*TimedOperationDelay)(
      _Inout_ DXGK_TIMED_OPERATION *Op, 
      _In_ KPROCESSOR_MODE WaitMode, 
      _In_ BOOLEAN Alertable, 
      _In_opt_ const LARGE_INTEGER *Interval);
  NTSTATUS               (*TimedOperationWaitForSingleObject)(
      _Inout_ DXGK_TIMED_OPERATION *Op, 
      _In_ PVOID Object, 
      _In_ KWAIT_REASON WaitReason, 
      _In_ KPROCESSOR_MODE WaitMode, 
      _In_ BOOLEAN Alertable, 
      _In_opt_ const LARGE_INTEGER *Timeout);
} DXGK_TIMED_OPERATION_INTERFACE, *PDXGK_TIMED_OPERATION_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>The version number of the <a href="display.timed_operation_interface">Timed Operation Interface</a>. Version number constants are defined in <i>Dispmprt.h</i> (for example, DXGK_TIMED_OPERATION_INTERFACE_VERSION_1).</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A pointer to a context that is provided by the display port driver.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>A pointer to an interface reference function that is implemented by the display port driver.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>A pointer to an interface dereference function that is implemented by the display port driver.</p>
</dd>

### -field <b>TimedOperationStart</b>

<dd>
<p>A pointer to the display port driver's <a href="display.timedoperationstart">TimedOperationStart</a> function. </p>
<dl>

### -field <i>Op</i>

<dd>
<p>See <a href="display.timedoperationstart">TimedOperationStart</a> for more information.</p>
</dd>

### -field <i>Timeout</i>

<dd>
<p>See <a href="display.timedoperationstart">TimedOperationStart</a> for more information.</p>
</dd>

### -field <i>OsHandled</i>

<dd>
<p>See <a href="display.timedoperationstart">TimedOperationStart</a> for more information.</p>
</dd>
</dl>
</dd>

### -field <b>TimedOperationDelay</b>

<dd>
<p>A pointer to the display port driver's <a href="display.timedoperationdelay">TimedOperationDelay</a> function. </p>
<dl>

### -field <i>Op</i>

<dd>
<p>See <a href="display.timedoperationdelay">TimedOperationDelay</a> for more information.</p>
</dd>

### -field <i>WaitMode</i>

<dd>
<p>See <a href="display.timedoperationdelay">TimedOperationDelay</a> for more information.</p>
</dd>

### -field <i>Alertable</i>

<dd>
<p>See <a href="display.timedoperationdelay">TimedOperationDelay</a> for more information.</p>
</dd>

### -field <i>Interval</i>

<dd>
<p>See <a href="display.timedoperationdelay">TimedOperationDelay</a> for more information.</p>
</dd>
</dl>
</dd>

### -field <b>TimedOperationWaitForSingleObject</b>

<dd>
<p>A pointer to the display port driver's <a href="display.timedoperationwaitforsingleobject">TimedOperationWaitForSingleObject</a> function. </p>
<dl>

### -field <i>Op</i>

<dd>
<p>See <a href="display.timedoperationwaitforsingleobject">TimedOperationWaitForSingleObject</a> for more information.</p>
</dd>

### -field <i>Object</i>

<dd>
<p>See <a href="display.timedoperationwaitforsingleobject">TimedOperationWaitForSingleObject</a> for more information.</p>
</dd>

### -field <i>WaitReason</i>

<dd>
<p>See <a href="display.timedoperationwaitforsingleobject">TimedOperationWaitForSingleObject</a> for more information.</p>
</dd>

### -field <i>WaitMode</i>

<dd>
<p>See <a href="display.timedoperationwaitforsingleobject">TimedOperationWaitForSingleObject</a> for more information.</p>
</dd>

### -field <i>Alertable</i>

<dd>
<p>See <a href="display.timedoperationwaitforsingleobject">TimedOperationWaitForSingleObject</a> for more information.</p>
</dd>

### -field <i>Timeout</i>

<dd>
<p>See <a href="display.timedoperationwaitforsingleobject">TimedOperationWaitForSingleObject</a> for more information.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The display miniport driver supplies the <b>Size</b> and <b>Version</b> members of this structure, and then calls <a href="..\dispmprt\nc-dispmprt-dxgkcb-query-services.md">DxgkCbQueryServices</a>, which fills in the remaining members of this structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb-query-services.md">DxgkCbQueryServices</a>
</dt>
<dt>
<a href="display.timed_operation_interface">Timed Operation Interface</a>
</dt>
<dt>
<a href="display.timedoperationdelay">TimedOperationDelay</a>
</dt>
<dt>
<a href="display.timedoperationstart">TimedOperationStart</a>
</dt>
<dt>
<a href="display.timedoperationwaitforsingleobject">TimedOperationWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_TIMED_OPERATION_INTERFACE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
