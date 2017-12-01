---
UID: NC.dot11wdi.MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE
title: MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE
author: windows-driver-content
description: The MiniportWdiAdapterHangDiagnose handler function is used to collect hardware control register states and optionally full firmware state.
old-location: netvista\miniportwdiadapterhangdiagnose.htm
old-project: netvista
ms.assetid: 233CCF43-481E-4759-A2FC-0329103F8208
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MiniportWdiAdapterHangDiagnose
req.alt-loc: dot11wdi.h
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
req.iface: ISynthSinkDMus
---

# MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE callback



## -description
<p>The MiniportWdiAdapterHangDiagnose handler function is used to collect hardware control register states and optionally full firmware state.</p>
<p>This is a WDI miniport handler inside <a href="..\dot11wdi\ns-dot11wdi--ndis-miniport-driver-wdi-characteristics.md">NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS</a>.</p>


## -prototype

````
MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE MiniportWdiAdapterHangDiagnose;

NDIS_STATUS MiniportWdiAdapterHangDiagnose(
  _In_  NDIS_HANDLE    MiniportDriverContext,
  _In_  eDiagnoseLevel DiagnoseLevel,
  _In_  UINT32         BufferSize,
  _Out_ UINT8          *FirmwareBlob,
  _Out_ UINT32         *pOutputSize
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportDriverContext</i> [in]

<dd>
<p>The handle to a driver-allocated context area where the driver maintains state and configuration information. The miniport driver passed this context area to the <a href="..\dot11wdi\nf-dot11wdi-ndismregisterwdiminiportdriver.md">NdisMRegisterWdiMiniportDriver</a> function.</p>
</dd>

### -param <i>DiagnoseLevel</i> [in]

<dd>
<p>The diagnose level, as defined in the <a href="..\dot11wdi\ne-dot11wdi-ediagnoselevel.md">eDiagnoseLevel</a> enumeration. The default level is <b>DiagnoseLevelHardwareRegisters</b>, 1KB maximum in the output buffer.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The size of <b>FirmwareBlob</b>, in bytes.</p>
</dd>

### -param <i>FirmwareBlob</i> [out]

<dd>
<p>A pointer to the buffer that  will contain the hardware control registry states, and optionally full firmware state.</p>
</dd>

### -param <i>pOutputSize</i> [out]

<dd>
<p>A pointer to the number of bytes written to <b>FirmwareBlob</b>.</p>
</dd>
</dl>

## -returns
<p>The return value is ignored.</p>

## -remarks
<p>    The default diagnose level is <b>DiagnoseLevelHardwareRegisters</b>, with 1KB maximum in the output buffer.</p>

<p>To define a MiniportWdiAdapterHangDiagnose function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a MiniportWdiAdapterHangDiagnose function that is named "MyAdapterHangDiagnose", use the <b>MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE</b> function type is defined in the dot11wdi.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dot11wdi\ne-dot11wdi-ediagnoselevel.md">eDiagnoseLevel</a>
</dt>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--ndis-miniport-driver-wdi-characteristics.md">NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS</a>
</dt>
<dt>
<a href="netvista.wdi_hang_detection_and_recovery">WDI hang detection and recovery</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
