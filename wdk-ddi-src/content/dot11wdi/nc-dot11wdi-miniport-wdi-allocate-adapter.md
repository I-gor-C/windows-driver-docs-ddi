---
UID: NC.dot11wdi.MINIPORT_WDI_ALLOCATE_ADAPTER
title: MINIPORT_WDI_ALLOCATE_ADAPTER
author: windows-driver-content
description: The MiniportWdiAllocateAdapter handler function allocates a WDI miniport adapter.
old-location: netvista\miniportwdiallocateadapter.htm
old-project: netvista
ms.assetid: 4CBC7230-6480-40C9-90B7-A286FCEB1FA8
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
req.alt-api: MiniportWdiAllocateAdapter
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

# MINIPORT_WDI_ALLOCATE_ADAPTER callback



## -description
<p>The MiniportWdiAllocateAdapter handler function allocates a WDI miniport adapter.</p>
<p>This is a WDI miniport handler inside <a href="..\dot11wdi\ns-dot11wdi--ndis-miniport-driver-wdi-characteristics.md">NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS</a>.</p>


## -prototype

````
MINIPORT_WDI_ALLOCATE_ADAPTER MiniportWdiAllocateAdapter;

NDIS_STATUS MiniportWdiAllocateAdapter(
  _In_    NDIS_HANDLE                                    NdisMiniportHandle,
  _In_    NDIS_HANDLE                                    MiniportDriverContext,
  _In_    PNDIS_MINIPORT_INIT_PARAMETERS                 MiniportInitParameters,
  _In_    PNDIS_WDI_INIT_PARAMETERS                      NdisWdiInitParameters,
  _Inout_ PNDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES RegistrationAttributes
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisMiniportHandle</i> [in]

<dd>
<p>The NDIS-supplied handle that identifies the miniport adapter.</p>
</dd>

### -param <i>MiniportDriverContext</i> [in]

<dd>
<p>The handle to a driver-allocated context area where the driver maintains state and configuration information. The miniport driver passed this context area to the <a href="..\dot11wdi\nf-dot11wdi-ndismregisterwdiminiportdriver.md">NdisMRegisterWdiMiniportDriver</a> function.

</p>
</dd>

### -param <i>MiniportInitParameters</i> [in]

<dd>
<p>A pointer to an <a href="..\ndis\ns-ndis--ndis-miniport-init-parameters.md">NDIS_MINIPORT_INIT_PARAMETERS</a> structure that defines the initialization parameters for the miniport adapter.</p>
</dd>

### -param <i>NdisWdiInitParameters</i> [in]

<dd>
<p>A pointer to an <a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-init-parameters.md">NDIS_WDI_INIT_PARAMETERS</a> structure that defines the WDI initialization parameters for the miniport adapter.</p>
</dd>

### -param <i>RegistrationAttributes</i> [in, out]

<dd>
<p>A pointer to an <a href="..\ndis\ns-ndis--ndis-miniport-adapter-registration-attributes.md">NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a> structure that defines registration attributes that are associated with the miniport adapter.</p>
</dd>
</dl>

## -returns
<p>
            MiniportWdiAllocateAdapter can return any of the following return values.</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>MiniportWdiAllocateAdapter successfully completed.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>MiniportWdiAllocateAdapter could not allocate the necessary resources.</p>

<p> </p>

<p>To define a MiniportWdiAllocateAdapter function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a MiniportWdiAllocateAdapter function that is named "MyAllocateAdapter", use the <b>MINIPORT_WDI_ALLOCATE_ADAPTER</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_WDI_ALLOCATE_ADAPTER</b> function type is defined in the dot11wdi.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_WDI_ALLOCATE_ADAPTER</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -remarks


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
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-registration-attributes.md">NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--ndis-miniport-driver-wdi-characteristics.md">NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-init-parameters.md">NDIS_MINIPORT_INIT_PARAMETERS</a>
</dt>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-init-parameters.md">NDIS_WDI_INIT_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_WDI_ALLOCATE_ADAPTER callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
