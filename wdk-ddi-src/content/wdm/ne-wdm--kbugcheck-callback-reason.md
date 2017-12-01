---
UID: NE.wdm._KBUGCHECK_CALLBACK_REASON
title: KBUGCHECK_CALLBACK_REASON
author: windows-driver-content
description: The KBUGCHECK_CALLBACK_REASON enumeration type specifies the situations in which a bug-check callback executes.
old-location: kernel\kbugcheck_callback_reason.htm
old-project: kernel
ms.assetid: 08246843-9b6e-4694-8475-acb02fbdd82b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Supported on Windows XP with Service Pack 1 (SP1), Windows Server 2003, and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KBUGCHECK_CALLBACK_REASON
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KBUGCHECK_CALLBACK_REASON enumeration



## -description
<p>The <b>KBUGCHECK_CALLBACK_REASON</b> enumeration type specifies the situations in which a bug-check callback executes.</p>


## -syntax

````
typedef enum _KBUGCHECK_CALLBACK_REASON { 
  KbCallbackInvalid            = 0,
  KbCallbackReserved1          = 1,
  KbCallbackSecondaryDumpData  = 2,
  KbCallbackDumpIo             = 3,
  KbCallbackAddPages           = 4
} KBUGCHECK_CALLBACK_REASON;
````


## -enum-fields
<dl>

### -field <a id="KbCallbackInvalid"></a><a id="kbcallbackinvalid"></a><a id="KBCALLBACKINVALID"></a><b>KbCallbackInvalid</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>

### -field <a id="KbCallbackReserved1"></a><a id="kbcallbackreserved1"></a><a id="KBCALLBACKRESERVED1"></a><b>KbCallbackReserved1</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>

### -field <a id="KbCallbackSecondaryDumpData"></a><a id="kbcallbacksecondarydumpdata"></a><a id="KBCALLBACKSECONDARYDUMPDATA"></a><b>KbCallbackSecondaryDumpData</b>

<dd>
<p>Specifies that the callback is executed to provide data that the system appends to the secondary section of the crash dump file. For more information about this type of callback, see <a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckSecondaryDumpDataCallback</a>.</p>
</dd>

### -field <a id="KbCallbackDumpIo"></a><a id="kbcallbackdumpio"></a><a id="KBCALLBACKDUMPIO"></a><b>KbCallbackDumpIo</b>

<dd>
<p>Specifies that the callback is executed each time a section of the dump file is written. For more information about this type of callback, see <a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckDumpIoCallback</a>.</p>
</dd>

### -field <a id="KbCallbackAddPages"></a><a id="kbcallbackaddpages"></a><a id="KBCALLBACKADDPAGES"></a><b>KbCallbackAddPages</b>

<dd>
<p>Specifies that the callback is executed to provide one or more pages of data that the system adds to the primary section of the crash dump file. For more information about this type of callback, see <a href="kernel.bugcheckaddpagescallback">BugCheckAddPagesCallback</a>. This enumeration value is supported in Windows Server 2008 and later versions of Windows.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported on Windows XP with Service Pack 1 (SP1), Windows Server 2003, and later versions of the Windows operating system.</p>
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
<a href="..\wdm\nf-wdm-keregisterbugcheckreasoncallback.md">KeRegisterBugCheckReasonCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551873">KBUGCHECK_REASON_CALLBACK_RECORD</a>
</dt>
<dt>
<a href="kernel.bugcheckaddpagescallback">BugCheckAddPagesCallback</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckDumpIoCallback</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckSecondaryDumpDataCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KBUGCHECK_CALLBACK_REASON enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
