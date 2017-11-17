---
UID: NS.compstui._EXTCHKBOX
title: EXTCHKBOX
author: windows-driver-content
description: The EXTCHKBOX structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended check box, which can be added to a property sheet page option.
old-location: print\extchkbox.htm
ms.assetid: b3b82474-d4e5-467c-93dc-30edac189c66
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: compstui.h
req.include-header: Compstui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EXTCHKBOX
req.alt-loc: compstui.h
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
ms.keywords: EXTCHKBOX, EXTCHKBOX, *PEXTCHKBOX
req.iface: 
---

# EXTCHKBOX structure



## -description
<p>The EXTCHKBOX structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended check box, which can be added to a property sheet page option.</p>


## -syntax

````
typedef struct _EXTCHKBOX {
  WORD      cbSize;
  WORD      Flags;
  LPTSTR    pTitle;
  LPTSTR    pSeparator;
  LPTSTR    pCheckedName;
  ULONG_PTR IconID;
  WORD      wReserved[4];
  ULONG_PTR dwReserved[2];
} EXTCHKBOX, *PEXTCHKBOX;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Size, in bytes, of the EXTCHKBOX structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Bit flags, which can be one of the following:</p>
<p></p>
<dl>

### -field <a id="ECBF_CHECKNAME_AT_FRONT"></a><a id="ecbf_checkname_at_front"></a>ECBF_CHECKNAME_AT_FRONT

<dd>
<p>If set, CPSUI displays strings in the order "pCheckedName pSeparator <i>SelectName</i>", where <i>SelectName</i> is the string associated with the option's selected value.</p>
<p>If not set, CPSUI displays strings in the order "<i>SelectName</i> pSeparator pCheckedName".</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ECBF_CHECKNAME_ONLY_ENABLED"></a><a id="ecbf_checkname_only_enabled"></a>ECBF_CHECKNAME_ONLY_ENABLED

<dd>
<p>If set, CPSUI displays the pCheckedName string only if the option is checked and enabled (that is, OPTIF_ECB_CHECKED is set and OPTIF_DISABLED is clear in the OPTITEM structure).</p>
<p>If not set, CPSUI always displays the pCheckedName string if the option is checked (that is, OPTIF_ECB_CHECKED is set in the OPTITEM structure), even if the option is disabled.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ECBF_ICONID_AS_HICON"></a><a id="ecbf_iconid_as_hicon"></a>ECBF_ICONID_AS_HICON

<dd>
<p>If set, the <b>IconID</b> member contains an icon handle.</p>
<p>If not set, the <b>IconID</b> member contains an icon resource identifier.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ECBF_OVERLAY_ECBICON_IF_CHECKED"></a><a id="ecbf_overlay_ecbicon_if_checked"></a>ECBF_OVERLAY_ECBICON_IF_CHECKED

<dd>
<p>If set, and if the check box is checked (that is, OPTIF_ECB_CHECKED is set in the OPTITEM structure), CPSUI overlays the icon identified by the <b>IconID</b> member onto the icon associated with the option item.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ECBF_OVERLAY_NO_ICON"></a><a id="ecbf_overlay_no_icon"></a>ECBF_OVERLAY_NO_ICON

<dd>
<p>If set, CPSUI overlays its IDI_CPSUI_NO icon onto the icon identified by the <b>IconID</b> member.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ECBF_OVERLAY_STOP_ICON"></a><a id="ecbf_overlay_stop_icon"></a>ECBF_OVERLAY_STOP_ICON

<dd>
<p>If set, CPSUI overlays the IDI_CPSUI_STOP icon onto the icon identified by the <b>IconID</b> member.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ECBF_OVERLAY_WARNING_ICON"></a><a id="ecbf_overlay_warning_icon"></a>ECBF_OVERLAY_WARNING_ICON

<dd>
<p>If set, CPSUI overlays its IDI_CPSUI_WARNING icon onto the icon identified by the <b>IconID</b> member.</p>
</dd>
</dl>
</dd>

### -field <b>pTitle</b>

<dd>
<p>String identifier, representing the check box title. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.</p>
</dd>

### -field <b>pSeparator</b>

<dd>
<p>String identifier, representing a separator character to be displayed between the checked name string and the selected option string This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.</p>
</dd>

### -field <b>pCheckedName</b>

<dd>
<p>String identifier, representing the text to be displayed when the check box is checked. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.</p>
</dd>

### -field <b>IconID</b>

<dd>
<p>One of the following icon identifiers:</p>
<ul>
<li>
<p>An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI_CPSUI-prefixed icon resource identifiers.</p>
</li>
<li>
<p>An icon handle. If a handle is specified, ECBF_ICONID_AS_HICON must be set in the <b>Flags</b> member.</p>
</li>
</ul>
<p>If this value is zero, an icon is not displayed.</p>
</dd>

### -field <b>wReserved</b>

<dd>
<p>Reserved, must be initialized to zero.</p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>Reserved, must be initialized to zero.</p>
</dd>
</dl>

## -remarks
<p>An extended check box is a CPSUI-defined type of check box that can be associated with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structure. An OPTITEM structure can have one extended check box or one extended push button associated with it.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Compstui.h (include Compstui.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548795">EXTPUSH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20EXTCHKBOX structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
