---
UID: NS.ntddchgr._CHANGER_SET_ACCESS
title: CHANGER_SET_ACCESS
author: windows-driver-content
description: The CHANGER_SET_ACCESS structure is used in conjunction with theIOCTL_CHANGER_SET_ACCESS request to set the state of the device's import/export port (IEport), door, or keypad.
old-location: storage\changer_set_access.htm
old-project: storage
ms.assetid: 4349d772-89c6-4201-9d9d-2e0590d61424
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: CHANGER_SET_ACCESS, CHANGER_SET_ACCESS, *PCHANGER_SET_ACCESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddchgr.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CHANGER_SET_ACCESS
req.alt-loc: ntddchgr.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# CHANGER_SET_ACCESS structure



## -description
<p>The CHANGER_SET_ACCESS structure is used in conjunction with the<a href="https://msdn.microsoft.com/library/windows/hardware/ff559422">IOCTL_CHANGER_SET_ACCESS</a> request to set the state of the device's import/export port (IEport), door, or keypad. </p>


## -syntax

````
typedef struct _CHANGER_SET_ACCESS {
  CHANGER_ELEMENT Element;
  ULONG           Control;
} CHANGER_SET_ACCESS, *PCHANGER_SET_ACCESS;
````


## -struct-fields
<dl>

### -field <b>Element</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551457">CHANGER_ELEMENT</a> structure that specifies the element type and the zero-based address of the element to set. The <b>ElementType</b> member of the CHANGER_ELEMENT structure must be assigned one of the following values:</p>
<p><b>ChangerIEPortChangerDoorChangerKeypad</b></p>
</dd>

### -field <b>Control</b>

<dd>
<p>Specifies the operation to perform on the element. The <b>Features0</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff554979">GET_CHANGER_PARAMETERS</a> indicates whether the changer supports a particular category of operation.</p>
<p></p>
<dl>

### -field <a id="LOCK_ELEMENT"></a><a id="lock_element"></a>LOCK_ELEMENT

<dd>
<p>Lock the door, IEport, or keypad. Valid only if CHANGER_LOCK_UNLOCK is set.</p>
</dd>

### -field <a id="UNLOCK_ELEMENT"></a><a id="unlock_element"></a>UNLOCK_ELEMENT

<dd>
<p>Unlock the door, IEport, or keypad. Valid only if CHANGER_LOCK_UNLOCK is set.</p>
</dd>

### -field <a id="EXTEND_IEPORT"></a><a id="extend_ieport"></a>EXTEND_IEPORT

<dd>
<p>Extend the IEport. Valid only if CHANGER_OPEN_IEPORT is set.</p>
</dd>

### -field <a id="RETRACT_IEPORT"></a><a id="retract_ieport"></a>RETRACT_IEPORT

<dd>
<p>Retract the IEport. Valid only if CHANGER_CLOSE_IEPORT is set.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddchgr.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559422">IOCTL_CHANGER_SET_ACCESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551447">ChangerSetAccess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554979">GET_CHANGER_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551457">CHANGER_ELEMENT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CHANGER_SET_ACCESS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
