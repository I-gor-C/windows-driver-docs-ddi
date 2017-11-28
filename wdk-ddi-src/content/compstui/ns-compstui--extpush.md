---
UID: NS.compstui._EXTPUSH
title: EXTPUSH
author: windows-driver-content
description: The EXTPUSH structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended push button, which can be added to a property sheet page option. When the button is pushed, a new dialog can be displayed.
old-location: print\extpush.htm
old-project: print
ms.assetid: c38d7eca-6486-4bb1-b0a8-7f69fe13f7db
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: EXTPUSH, EXTPUSH, *PEXTPUSH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: compstui.h
req.include-header: Compstui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EXTPUSH
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
req.iface: 
---

# EXTPUSH structure



## -description
<p>The EXTPUSH structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended push button, which can be added to a property sheet page option. When the button is pushed, a new dialog can be displayed.</p>


## -syntax

````
typedef struct _EXTPUSH {
  WORD      cbSize;
  WORD      Flags;
  LPTSTR    pTitle;
  union {
    DLGPROC DlgProc;
    FARPROC pfnCallBack;
  };
  ULONG_PTR IconID;
  union {
    WORD   DlgTemplateID;
    HANDLE hDlgTemplate;
  };
  ULONG_PTR dwReserved[3];
} EXTPUSH, *PEXTPUSH;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Size, in bytes, of the EXTPUSH structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Bit flags, which can be one of the following:</p>
<p></p>
<dl>

### -field <a id="EPF_ICONID_AS_HICON"></a><a id="epf_iconid_as_hicon"></a>EPF_ICONID_AS_HICON

<dd>
<p>If set, the <b>IconID</b> member contains an icon handle.</p>
<p>If not set, the <b>IconID</b> member contains an icon resource identifier.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="EPF_INCLUDE_SETUP_TITLE"></a><a id="epf_include_setup_title"></a>EPF_INCLUDE_SETUP_TITLE

<dd>
<p>If set, CPSUI appends "Setup" to the string pointed to by <b>pTitle</b>.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="EPF_NO_DOT_DOT_DOT"></a><a id="epf_no_dot_dot_dot"></a>EPF_NO_DOT_DOT_DOT

<dd>
<p>If set, CPSUI does not append "..." to the string pointed to by <b>pTitle</b>.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="EPF_OVERLAY_NO_ICON"></a><a id="epf_overlay_no_icon"></a>EPF_OVERLAY_NO_ICON

<dd>
<p>If set, CPSUI overlays its IDI_CPSUI_NO icon onto the icon identified by the <b>IconID</b> member.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="EPF_OVERLAY_STOP_ICON"></a><a id="epf_overlay_stop_icon"></a>EPF_OVERLAY_STOP_ICON

<dd>
<p>If set, CPSUI overlays the IDI_CPSUI_STOP icon onto the icon identified by the <b>IconID</b> member.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="EPF_OVERLAY_WARNING_ICON"></a><a id="epf_overlay_warning_icon"></a>EPF_OVERLAY_WARNING_ICON

<dd>
<p>If set, CPSUI overlays its IDI_CPSUI_WARNING icon onto the icon identified by the <b>IconID</b> member.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="EPF_PUSH_TYPE_DLGPROC"></a><a id="epf_push_type_dlgproc"></a>EPF_PUSH_TYPE_DLGPROC

<dd>
<p>If set, the <b>DlgProc</b> and <b>DlgTemplateID/hDlgTemplate</b> members are valid.</p>
<p>If not set, the <b>pfnCallBack</b> member is valid.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="EPF_USE_HDLGTEMPLATE"></a><a id="epf_use_hdlgtemplate"></a>EPF_USE_HDLGTEMPLATE

<dd>
<p>If set, <b>hDlgTemplate</b> contains a template handle.</p>
<p>If not set, <b>DlgTemplateID</b> contains a template resource identifier.</p>
</dd>
</dl>
</dd>

### -field <b>pTitle</b>

<dd>
<p>String identifier, representing the push button title. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.</p>
</dd>

### -field <b>DlgProc</b>

<dd>
<p>DLGPROC-typed pointer to a dialog box procedure to process messages for the push button's dialog box. (The DLGPROC pointer type is described in the Microsoft Windows SDK documentation.) For more information, see the following Remarks section.</p>
<p>If this pointer is supplied, EPF_PUSH_TYPE_DLGPROC must be set in <b>Flags</b>.</p>
</dd>

### -field <b>pfnCallBack</b>

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313">_CPSUICALLBACK</a>-typed callback function to handle the CPSUICB_REASON_PUSHBUTTON reason. For more information, see the following Remarks section.</p>
<p>If this pointer is supplied, EPF_PUSH_TYPE_DLGPROC must be cleared in <b>Flags</b>.</p>
</dd>

### -field <b>IconID</b>

<dd>
<p>One of the following icon identifiers:</p>
<ul>
<li>
<p>An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI_CPSUI-prefixed icon resource identifiers.</p>
</li>
<li>
<p>An icon handle. If a handle is specified, EPF_ICONID_AS_HICON must be set in the <b>Flags</b> member.</p>
</li>
</ul>
<p>CPSUI displays the icon next to the push button. If this value is zero, an icon is not displayed.</p>
</dd>

### -field <b>DlgTemplateID</b>

<dd>
<p>DIALOG resource identifier, describing a dialog box template.</p>
<p>Not used if EPF_USE_HDLGTEMPLATE is set in <b>Flags</b>.</p>
</dd>

### -field <b>hDlgTemplate</b>

<dd>
<p>Handle to a DLGTEMPLATE structure (described in the Microsoft Windows SDK documentation).</p>
<p>Used only if EPF_USE_HDLGTEMPLATE is set in <b>Flags</b>.</p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>Reserved, must be initialized to zero.</p>
</dd>
</dl>

## -remarks
<p>An extended push button is a CPSUI-defined type of push button that can be associated with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structure. An OPTITEM structure can have one extended push button or one extended check box associated with it.</p>

<p>When you use the EXTPUSH structure to create a push button, you can optionally create an additional dialog box that opens when the user clicks on the button. To create this dialog box, you should specify a pointer to a dialog box procedure in the <b>DlgProc</b> member, and include a dialog template specification in either the <b>DlgTemplateID</b> or the <b>hDlgTemplate</b> member.</p>

<p>If EPF_USE_HDLGTEMPLATE is set in <b>Flags</b>, CPSUI creates the dialog box by calling <b>DialogBoxIndirectParam</b> (described in the Windows SDK documentation), passing the contents of the <b>DlgProc</b> and <b>hDlgTemplate</b> members.</p>

<p>If EPF_USE_HDLGTEMPLATE is not set in <b>Flags</b>, CPSUI creates the dialog box by calling <b>DialogBoxParam</b> (described in the Windows SDK documentation), passing the contents of the <b>DlgProc</b> and <b>DlgTemplateID</b> members.</p>

<p>When the dialog box procedure is called with a <i>uMsg</i> value of WM_INITDIALOG, the <i>lParam</i> value is the address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547088">CPSUICBPARAM</a> structure, with the <b>Reason</b> member set to CPSUICB_REASON_EXTPUSH. (For more information about the <i>uMsg</i> and <i>lParam</i> parameters, see <b>DialogProc</b> in the Windows SDK documentation.)</p>

<p>If you do not need CPSUI to display a dialog box when the user clicks on the button, you can specify the address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313">_CPSUICALLBACK</a>-typed callback function in the <b>pfnCallBack</b> member. When a user clicks on the button, CPSUI calls the callback function. The accompanying CPSUICBPARAM structure's <b>Reason</b> member will be set to CPSUICB_REASON_EXTPUSH.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548781">EXTCHKBOX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20EXTPUSH structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
