---
UID: NF.ndis.NdisFRegisterFilterDriver
title: NdisFRegisterFilterDriver
author: windows-driver-content
description: A filter driver calls the NdisFRegisterFilterDriver function to register its FilterXxx functions with NDIS.
old-location: netvista\ndisfregisterfilterdriver.htm
old-project: netvista
ms.assetid: 14381de2-36d9-4ec8-9d4e-7af3e6d8ecf3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisFRegisterFilterDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFRegisterFilterDriver
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Filter_Driver_Function, NdisFDeregisterFilterDriver
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisFRegisterFilterDriver function



## -description
<p>A filter driver calls the
  <b>
    NdisFRegisterFilterDriver</b> function to register its 
  <i>FilterXxx</i> functions with NDIS.</p>


## -syntax

````
NDIS_STATUS NdisFRegisterFilterDriver(
  _In_  PDRIVER_OBJECT                      DriverObject,
  _In_  NDIS_HANDLE                         FilterDriverContext,
  _In_  PNDIS_FILTER_DRIVER_CHARACTERISTICS FilterCharacteristics,
  _Out_ PNDIS_HANDLE                        NdisFilterDriverHandle
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to an opaque driver object that the filter driver received in its 
     <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine at the 
     <i>Argument1</i> parameter. (For more information, see 
     <a href="netvista.driverentry_of_ndis_filter_drivers">DriverEntry of NDIS Filter
     Drivers</a>.)</p>
</dd>

### -param <i>FilterDriverContext</i> [in]

<dd>
<p>A handle to a driver-allocated context area where the driver maintains state and configuration
     information.</p>
</dd>

### -param <i>FilterCharacteristics</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-filter-driver-characteristics.md">
     NDIS_FILTER_DRIVER_CHARACTERISTICS</a> structure that the filter driver created and initialized with
     its 
     <i>FilterXxx</i> function entry points.</p>
</dd>

### -param <i>NdisFilterDriverHandle</i> [out]

<dd>
<p>A pointer to a handle variable. If the call to 
     <b>
    NdisFRegisterFilterDriver</b> succeeds, NDIS fills this variable with a filter driver handle. The
     filter driver saves this handle and later passes this handle to NDIS functions, such as 
     <a href="..\ndis\nf-ndis-ndisfderegisterfilterdriver.md">NdisFDeregisterFilterDriver</a>,
     that require a filter driver handle as an input parameter.</p>
</dd>
</dl>

## -returns
<p><b>
    NdisFRegisterFilterDriver</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> returns NDIS_STATUS_SUCCESS if it registered the filter driver.</p><dl>
<dt><b>NDIS_STATUS_BAD_VERSION</b></dt>
</dl><p>The version that is specified in the 
       <b>MajorNdisVersion</b> member of the structure at 
       <i>FilterCharacteristics</i> is invalid.</p><dl>
<dt><b>NDIS_STATUS_BAD_CHARACTERISTICS</b></dt>
</dl><p>At least one of the members that are specified in 
       <a href="..\ndis\ns-ndis--ndis-filter-driver-characteristics.md">
       NDIS_FILTER_DRIVER_CHARACTERISTICS</a> is invalid.</p><dl>
<dt><b>NDIS_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>At least one of the input parameters that the driver passed to 
       <a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> is invalid.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> failed because of insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> returns NDIS_STATUS_FAILURE if none of the preceding values
       applies.</p>

<p> </p>

## -remarks
<p>A filter driver calls the 
    <b>
    NdisFRegisterFilterDriver</b> function from its 
    <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. For more information about 
    <b>DriverEntry</b>, see 
    <a href="netvista.driverentry_of_ndis_filter_drivers">DriverEntry of NDIS Filter
    Drivers</a>.</p>

<p>Drivers that call <b>
    NdisFRegisterFilterDriver</b> must be prepared for an immediate call to any of their <i>FilterXxx</i> functions. For more information see <a href="NULL">Initializing a Filter Driver</a>.</p>

<p>Every filter driver exports a set of 
    <i>FilterXxx</i> functions by setting up the 
    <a href="..\ndis\ns-ndis--ndis-filter-driver-characteristics.md">
    NDIS_FILTER_DRIVER_CHARACTERISTICS</a> structure and calling 
    <b>
    NdisFRegisterFilterDriver</b>. NDIS copies this structure to the NDIS library's internal storage.</p>

<p>To allow filter drivers to register optional services, NDIS calls the 
    <a href="netvista.filtersetoptions">FilterSetOptions</a> function within the
    context of 
    <b>
    NdisFRegisterFilterDriver</b>.</p>

<p>After it has registered, a filter driver can later call the 
    <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> function
    to change the entry points for optional 
    <i>FilterXxx</i> functions.</p>

<p>Filter drivers call the 
    <a href="..\ndis\nf-ndis-ndisfderegisterfilterdriver.md">
    NdisFDeregisterFilterDriver</a> function to release resources that were previously allocated with 
    <b>
    NdisFRegisterFilterDriver</b>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_filter_driver_function">Irql_Filter_Driver_Function</a>, <a href="..\ndis\nf-ndis-ndisfderegisterfilterdriver.md">NdisFDeregisterFilterDriver</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.driverentry_of_ndis_filter_drivers">DriverEntry of NDIS Filter
   Drivers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-filter-driver-characteristics.md">
   NDIS_FILTER_DRIVER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfderegisterfilterdriver.md">NdisFDeregisterFilterDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="NULL">Initializing a Filter Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFRegisterFilterDriver function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
