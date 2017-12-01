---
UID: NS.d3dkmthk._D3DKMT_ESCAPE
title: D3DKMT_ESCAPE
author: windows-driver-content
description: The D3DKMT_ESCAPE structure describes information that is exchanged with the display miniport driver.
old-location: display\d3dkmt_escape.htm
old-project: display
ms.assetid: db57ae5e-7060-4d45-99a5-e54c82b0aa05
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_ESCAPE, D3DKMT_ESCAPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_ESCAPE
req.alt-loc: d3dkmthk.h
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

# D3DKMT_ESCAPE structure



## -description
<p>The D3DKMT_ESCAPE structure describes information that is exchanged with the display miniport driver.</p>


## -syntax

````
typedef struct _D3DKMT_ESCAPE {
  D3DKMT_HANDLE      hAdapter;
  D3DKMT_HANDLE      hDevice;
  D3DKMT_ESCAPETYPE  Type;
  D3DDDI_ESCAPEFLAGS Flags;
  VOID               *pPrivateDriverData;
  UINT               PrivateDriverDataSize;
  D3DKMT_HANDLE      hContext;
} D3DKMT_ESCAPE;
````


## -struct-fields
<dl>

### -field <b>hAdapter</b>

<dd>
<p>[in] A handle to the graphics adapter that information is exchanged on.</p>
</dd>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to a display device that is optionally specified if the information to be exchanged is specific to a particular device.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>[in] A value of type D3DKMT_ESCAPETYPE that indicates either to exchange information with the display miniport driver or to control kernel-mode components. The following table shows the possible values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DRIVERPRIVATE (0)</p>
</td>
<td>
<p>The <b>pPrivateDriverData</b> member is targeted at the display miniport driver. The hardware vendor defines the format of the escape data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_VIDMM (1)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>The OpenGL ICD controls the video memory manager (which is part of <i>Dxgkrnl.sys</i>). The buffer that <b>pPrivateDriverData</b> points to contains a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-vidmm-escape.md">D3DKMT_VIDMM_ESCAPE</a> structure that supports various types of control of the video memory manager.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_TDRDBGCTRL (2)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>The escape operation lets the user control the behavior of the operating system's Timeout Detection and Recovery (TDR) process. </p>
<p>This functionality is disabled by default. To enable this functionality, the TdrTestMode<b></b> = TdrTestMode DWORD registry value, which is stored in the HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers key, must be set to 1.</p>
<p>The <b>PrivateDriverDataSize</b> member is set to <b>sizeof</b>(int). The <b>pPrivateDriverData</b> member is set to an integer with a value from the <a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-tdrdbgctrltype.md">D3DKMT_TDRDBGCTRLTYPE</a> enumeration type.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_VIDSCH (3)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>The OpenGL ICD controls the graphics processing unit (GPU) scheduler (which is part of <i>Dxgkrnl.sys</i>). The buffer that <b>pPrivateDriverData</b> points to contains a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-vidsch-escape.md">D3DKMT_VIDSCH_ESCAPE</a> structure that supports preemption control and suspending or resuming the scheduler.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DEVICE (4)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>The OpenGL ICD controls the display device. The buffer that <b>pPrivateDriverData</b> points to contains a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-device-escape.md">D3DKMT_DEVICE_ESCAPE</a> structure that supports obtaining the video present source from the primary allocation.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DMM (5)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>The OpenGL ICD controls the display mode manager. The buffer that <b>pPrivateDriverData</b> points to contains a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-dmm-escape.md">D3DKMT_DMM_ESCAPE</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DEBUG_SNAPSHOT (6)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>The OpenGL ICD retrieves a debug snapshot buffer. The buffer that <b>pPrivateDriverData</b> points to contains a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-debug-snapshot-escape.md">D3DKMT_DEBUG_SNAPSHOT_ESCAPE</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_SETDRIVERUPDATESTATUS (7)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>The OpenGL ICD sets the display miniport driver update status. </p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DRT_TEST (8)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DIAGNOSTICS (9)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_OUTPUTDUPL_SNAPSHOT (10)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_OUTPUTDUPL_DIAGNOSTICS  (11)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_BDD_PNP (12)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_BDD_FALLBACK (13)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_ACTIVATE_SPECIFIC_DIAG(14)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_MODES_PRUNED_OUT(15)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_WQHL_INFO(16)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>        D3DKMT_ESCAPE_BRIGHTNESS(17)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>    D3DKMT_ESCAPE_EDID_CACHE(18)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_GENERIC_ADAPTER_DIAG_INFO(19)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_MIRACAST_DISPLAY_REQUEST (20)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_HISTORY_BUFFER_STATUS (21)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_MIRACAST_ADAPTER_DIAG_INFO (23)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_WIN32K_START(1024)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_WIN32K_HIP_DEVICE_INFO(1024)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_WIN32K_QUERY_CD_ROTATION_BLOCK (1025)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_WIN32K_DPI_INFO (1026)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_WIN32K_PRESENTER_VIEW_INFO (1027)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_WIN32K_SYSTEM_DPI (1028)</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>Supported starting with Windows 8.1.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-escapeflags.md">D3DDDI_ESCAPEFLAGS</a> structure that indicates, in bit-field flags, how to share information. The OpenGL ICD should specify the <b>HardwareAccess</b> bit-field flag to indicate that the display miniport driver must access graphics hardware in such a way that the operating system must perform the <a href="https://msdn.microsoft.com/2b7c1eae-6527-469e-a2fa-74d2a1246bd3">second level of synchronization</a> into the display miniport driver for the <a href="display.dxgkddiescape">DxgkDdiEscape</a> call. </p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[in/out] A pointer to a buffer that the OpenGL ICD allocates that contains information that the OpenGL ICD either exchanges with the display miniport driver or uses to control kernel-mode components. The following table describes the content of the buffer that <b>pPrivateDriverData</b> points to, depending on the value of <b>Type</b>.</p>
<table>
<tr>
<th>Value of the Type member</th>
<th>Content of the pPrivateDriverData buffer</th>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DRIVERPRIVATE</p>
</td>
<td>
<p>Driver-specific. The buffer is not usable unless a tight coupling exists between the OpenGL ICD and the display miniport driver.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_VIDMM</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-vidmm-escape.md">D3DKMT_VIDMM_ESCAPE</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_TDRDBGCTRL</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>A <a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-tdrdbgctrltype.md">D3DKMT_TDRDBGCTRLTYPE</a> enumeration type.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_VIDSCH</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-vidsch-escape.md">D3DKMT_VIDSCH_ESCAPE</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DEVICE</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-device-escape.md">D3DKMT_DEVICE_ESCAPE</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DMM</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-dmm-escape.md">D3DKMT_DMM_ESCAPE</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_ESCAPE_DEBUG_SNAPSHOT</p>
</td>
<td>
<p><b>Do not use. For testing purposes only.</b></p>
<p>A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-debug-snapshot-escape.md">D3DKMT_DEBUG_SNAPSHOT_ESCAPE</a> structure.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>[in] The size, in bytes, of the buffer that <b>pPrivateDriverData</b> points to. The OpenGL ICD must specify the size of the buffer when it calls the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtescape.md">D3DKMTEscape</a> function.</p>
</dd>

### -field <b>hContext</b>

<dd>
<p>[in] A handle to a context that is optionally specified if the information to be exchanged is specific to a particular device context. If the OpenGL ICD sets <b>hContext</b> to a non-NULL value, the ICD must have also set <b>hDevice</b> to a non-NULL value, and <b>hDevice</b> must correspond to the device that owns the context.</p>
</dd>
</dl>

## -remarks
<p>For testing purposes, the OpenGL ICD can pass a pointer to a D3DKMT_ESCAPE structure in a call to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtescape.md">D3DKMTEscape</a> function to control the video memory manager and GPU scheduler (which are part of <i>Dxgkrnl.sys</i>) and the behavior of the operating system's TDR process. </p>

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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-debug-snapshot-escape.md">D3DKMT_DEBUG_SNAPSHOT_ESCAPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-device-escape.md">D3DKMT_DEVICE_ESCAPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-dmm-escape.md">D3DKMT_DMM_ESCAPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-tdrdbgctrltype.md">D3DKMT_TDRDBGCTRLTYPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-vidmm-escape.md">D3DKMT_VIDMM_ESCAPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-vidsch-escape.md">D3DKMT_VIDSCH_ESCAPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtescape.md">D3DKMTEscape</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_ESCAPE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
