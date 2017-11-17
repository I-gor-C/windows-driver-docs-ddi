---
UID: NF.wdm.ExInitializeLookasideListEx
title: ExInitializeLookasideListEx
author: windows-driver-content
description: The ExInitializeLookasideListEx routine initializes a lookaside list.
old-location: kernel\exinitializelookasidelistex.htm
ms.assetid: 2f6072d2-808b-452f-a789-0c6f63195440
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExInitializeLookasideListEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (see Remarks section)
ms.keywords: ExInitializeLookasideListEx
req.iface: 
req.product: Windows 10 or later.
---

# ExInitializeLookasideListEx function



## -description
<p>The <b>ExInitializeLookasideListEx</b> routine initializes a lookaside list.</p>


## -syntax

````
NTSTATUS ExInitializeLookasideListEx(
  _Out_    PLOOKASIDE_LIST_EX    Lookaside,
  _In_opt_ PALLOCATE_FUNCTION_EX Allocate,
  _In_opt_ PFREE_FUNCTION_EX     Free,
  _In_     POOL_TYPE             PoolType,
  _In_     ULONG                 Flags,
  _In_     SIZE_T                Size,
  _In_     ULONG                 Tag,
  _In_     USHORT                Depth
);
````


## -parameters
<dl>

### -param <i>Lookaside</i> [out]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554329">LOOKASIDE_LIST_EX</a> structure to initialize. On return, this structure describes an empty lookaside list. The caller must use nonpaged system space for this structure, regardless of whether the entries in the lookaside list are allocated from paged or nonpaged memory. On 64-bit platforms, this structure must be 16-byte aligned.</p>
</dd>

### -param <i>Allocate</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554322">LookasideListAllocateEx</a> routine that allocates a new lookaside-list entry. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff544381">ExAllocateFromLookasideListEx</a> routine calls this <i>LookasideListAllocateEx</i> routine if the lookaside list is empty (contains no entries). This parameter is optional and can be specified as <b>NULL</b> if a custom allocation routine is not required. If this parameter is <b>NULL</b>, calls to <b>ExAllocateFromPagedLookasideList</b> automatically allocate the paged or nonpaged storage (as determined by the <i>PoolType</i> parameter) for the new entries.</p>
</dd>

### -param <i>Free</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554324">LookasideListFreeEx</a> routine that frees a previously allocated lookaside-list entry. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff544605">ExFreeToPagedLookasideList</a> routine calls this <i>LookasideListFreeEx</i> routine if the lookaside list is full (that is, the list already contains the maximum number of entries, as determined by the operating system). This parameter is optional and can be specified as <b>NULL</b> if a custom deallocation routine is not required. If this parameter is <b>NULL</b>, calls to <b>ExFreeToPagedLookasideList</b> automatically free the storage for the specified entries.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Specifies the pool type of the entries in the lookaside list. Set this parameter to a valid <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a> enumeration value.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies an optional flag value to modify the default behavior of the <i>LookasideListAllocateEx</i> routine. Set this parameter to zero or to one of the following EX_LOOKASIDE_LIST_EX_FLAGS_<i>XXX</i> flag bits.</p>
<table>
<tr>
<th>Flag bit</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>EX_LOOKASIDE_LIST_EX_FLAGS_RAISE_ON_FAIL</p>
</td>
<td>
<p>If the allocation fails, raise an exception.</p>
</td>
</tr>
<tr>
<td>
<p>EX_LOOKASIDE_LIST_EX_FLAGS_FAIL_NO_RAISE</p>
</td>
<td>
<p>If the allocation fails, return <b>NULL</b> instead of raising an exception. This flag is intended for use with an allocation routine, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff544513">ExAllocatePoolWithQuotaTag</a>, that charges quotas for pool usage. </p>
</td>
</tr>
</table>
<p> </p>
<p>These two flag bits are mutually exclusive.</p>
<p>If <i>Allocate</i> is <b>NULL</b>, set <i>Flags</i> to either zero or EX_LOOKASIDE_LIST_EX_FLAGS_RAISE_ON_FAIL, but not to EX_LOOKASIDE_LIST_EX_FLAGS_FAIL_NO_RAISE. Otherwise, the behavior of the default allocation routine is undefined.</p>
<p>If <i>Flags</i> = EX_LOOKASIDE_LIST_EX_FLAGS_RAISE_ON_FAIL, the <i>PoolType</i> parameter value is bitwise ORed with the POOL_RAISE_IF_ALLOCATION_FAILURE flag bit to form the <i>PoolType</i> parameter value that is passed to the <i>LookasideListAllocateEx</i> routine. The <i>LookasideListAllocateEx</i> routine can pass this <i>PoolType</i> value, without modification, to the <b>ExAllocatePoolWithTag</b> routine. For more information about the POOL_RAISE_IF_ALLOCATION_FAILURE flag, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>.</p>
<p>If <i>Flags</i> = EX_LOOKASIDE_LIST_EX_FLAGS_FAIL_NO_RAISE, the <i>PoolType</i> parameter value is bitwise ORed with the POOL_QUOTA_FAIL_INSTEAD_OF_RAISE flag bit to form the <i>PoolType</i> parameter value that is passed to the <i>LookasideListAllocateEx</i> routine. The <i>LookasideListAllocateEx</i> routine can pass this <i>PoolType</i> value, without modification, to the <b>ExAllocatePoolWithQuotaTag</b> routine. For more information about the POOL_QUOTA_FAIL_INSTEAD_OF_RAISE flag, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544513">ExAllocatePoolWithQuotaTag</a>. </p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Specifies the size, in bytes, of each entry in the lookaside list.</p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>Specifies the four-byte pool tag to use to mark the allocated storage for lookaside-list entries. For more information about pool tags, see the description of the <i>Tag</i> parameter in <b>ExAllocatePoolWithTag</b>. </p>
</dd>

### -param <i>Depth</i> [in]

<dd>
<p>Reserved. Always set this parameter to zero.</p>
</dd>
</dl>

## -returns
<p><b>ExInitializeLookasideListEx</b> returns STATUS_SUCCESS if the call is successful. Possible return values include the following error code:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_4</b></dt>
</dl><p>The <i>PoolType</i> parameter value is not valid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_5</b></dt>
</dl><p>The <i>Flags</i> parameter value is not valid.</p>

<p> </p>

## -remarks
<p>A driver must call this routine to initialize a lookaside list before the driver can begin to use the list. A lookaside list is a pool of fixed-size buffers that the driver can manage locally to reduce the number of calls to system allocation routines and, thereby, to improve performance. The buffers are stored as entries in the lookaside list. All entries in the list are of the same, uniform size, which is specified by the <i>Size</i> parameter.</p>

<p>After <b>ExInitializeLookasideListEx</b> returns, the lookaside list is initialized but contains no entries. When a client calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544381">ExAllocateFromLookasideListEx</a> routine to request an entry, this routine determines that the lookaside list is empty and calls the driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554322">LookasideListAllocateEx</a> routine to dynamically allocate storage for a new entry. Additional entries might be allocated in response to similar requests from clients. Later, when clients call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544597">ExFreeToLookasideListEx</a> to release these entries, this routine inserts the entries into the lookaside list. If the number of entries in the list reaches a limit that is determined by the operating system, <b>ExFreeToLookasideListEx</b> ceases to add further entries to the list and instead passes these entries to the driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554324">LookasideListFreeEx</a> routine to be freed.</p>

<p>If the driver does not supply <i>LookasideListAllocateEx</i> and <i>LookasideListFreeEx</i> routines, the <b>ExAllocateFromLookasideListEx</b> and <b>ExFreeToLookasideListEx</b> routines use default allocation and deallocation routines instead.</p>

<p>There is no benefit to providing <i>LookasideListAllocateEx</i> and <i>LookasideListFreeEx</i> routines that do nothing but call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>. The same effect can be achieved with better performance by simply setting the <i>Allocate</i> and <i>Free</i> parameters to <b>NULL</b>.</p>

<p>Before a driver unloads, it must explicitly free any lookaside lists it created. Failure to do so is a serious programming error. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544563">ExDeleteLookasideListEx</a> routine to free a lookaside list. This routine frees the storage for any remaining entries in the specified lookaside list and then removes the list from the system-wide set of active lookaside lists.</p>

<p>The operating system keeps track of all lookaside lists that are currently in use. As both the amount of available nonpaged memory and the demand for lookaside list entries vary over time, the operating system dynamically adjusts its limits for the maximum number of entries in each nonpaged lookaside list.</p>

<p>In Windows 2000 and later versions of Windows, a lookaside list that contains paged or nonpaged entries can be described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff558775">PAGED_LOOKASIDE_LIST</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff556431">NPAGED_LOOKASIDE_LIST</a> structure, respectively.</p>

<p>For more information about lookaside lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

<p>Callers of <b>ExInitializeLookasideListEx</b> can be running at IRQL &lt;= DISPATCH_LEVEL, but are typically running at IRQL = PASSIVE_LEVEL.</p>

<p>The driver-supplied <i>LookasideListAllocateEx</i> and <i>LookasideListFreeEx</i> routines both receive <i>Lookaside</i> parameters that point to the <b>LOOKASIDE_LIST_EX</b> structure that describes the lookaside list. The routines can use this parameter to access private data that the driver has associated with the lookaside list. For example, the driver might allocate an instance of the following structure to collect private data for each lookaside list that it creates:</p>

<p>The driver can initialize a lookaside list as shown in the following code example:</p>

<p>The following code example shows how the <i>LookasideListAllocateEx</i> routine can use its <i>Lookaside</i> parameter to access the private data that is associated with the lookaside list:</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a> macro is defined in the Ntdef.h header file. The <i>LookAsideListFreeEx</i> routine can similarly use its <i>Lookaside</i> parameter to access private data.</p>

<p>After the <code>MyLookasideListAllocateEx</code> routine in this example returns, <b>ExAllocateFromLookasideListEx</b> inserts the buffer pointed to by the <code>NewEntry</code> variable into the lookaside list. To make this insertion operation thread-safe, <b>ExAllocateFromLookasideListEx</b> synchronizes its access of the lookaside list with other list insertion and removal operations that might be performed by other threads. Similarly, when <b>ExFreeFromLookasideListEx</b> removes a buffer from the lookaside list, it synchronizes its access to the list.</p>

<p><b>ExAllocateFromLookasideListEx</b> and <b>ExFreeFromLookasideListEx</b> do not synchronize their calls to driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554322">LookasideListAllocateEx</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554324">LookasideListFreeEx</a> routines. Thus, if the <code>MyLookasideListAllocateEx</code> and <code>MyLookasideListFreeEx</code> routines in the preceding code examples must be thread-safe, the driver must provide the necessary synchronization.</p>

<p>The example routine, <code>MyLookasideListAllocateEx</code>, synchronizes its access of the <code>MyContext-&gt;NumberOfAllocations</code> variable with other threads that might increment and decrement this variable. To provide this synchronization, <code>MyLookasideListAllocateEx</code> calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547910">InterlockedIncrement</a> routine to atomically increment this variable. Similarly, the <code>MyLookasideListFreeEx</code> routine (not shown) can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547871">InterlockedDecrement</a> routine to atomically decrement this variable.</p>

<p>However, if the sole purpose of the <code>MyContext-&gt;NumberOfAllocations</code> variable in the preceding code example is simply to gather statistics on lookaside list allocations, atomic increments and decrements are hardly necessary. In this case, the remote possibility of a missed increment or decrement should not be a concern.</p>

<p>For more information about thread safety for lookaside lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

<p>A driver must call this routine to initialize a lookaside list before the driver can begin to use the list. A lookaside list is a pool of fixed-size buffers that the driver can manage locally to reduce the number of calls to system allocation routines and, thereby, to improve performance. The buffers are stored as entries in the lookaside list. All entries in the list are of the same, uniform size, which is specified by the <i>Size</i> parameter.</p>

<p>After <b>ExInitializeLookasideListEx</b> returns, the lookaside list is initialized but contains no entries. When a client calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544381">ExAllocateFromLookasideListEx</a> routine to request an entry, this routine determines that the lookaside list is empty and calls the driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554322">LookasideListAllocateEx</a> routine to dynamically allocate storage for a new entry. Additional entries might be allocated in response to similar requests from clients. Later, when clients call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544597">ExFreeToLookasideListEx</a> to release these entries, this routine inserts the entries into the lookaside list. If the number of entries in the list reaches a limit that is determined by the operating system, <b>ExFreeToLookasideListEx</b> ceases to add further entries to the list and instead passes these entries to the driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554324">LookasideListFreeEx</a> routine to be freed.</p>

<p>If the driver does not supply <i>LookasideListAllocateEx</i> and <i>LookasideListFreeEx</i> routines, the <b>ExAllocateFromLookasideListEx</b> and <b>ExFreeToLookasideListEx</b> routines use default allocation and deallocation routines instead.</p>

<p>There is no benefit to providing <i>LookasideListAllocateEx</i> and <i>LookasideListFreeEx</i> routines that do nothing but call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>. The same effect can be achieved with better performance by simply setting the <i>Allocate</i> and <i>Free</i> parameters to <b>NULL</b>.</p>

<p>Before a driver unloads, it must explicitly free any lookaside lists it created. Failure to do so is a serious programming error. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544563">ExDeleteLookasideListEx</a> routine to free a lookaside list. This routine frees the storage for any remaining entries in the specified lookaside list and then removes the list from the system-wide set of active lookaside lists.</p>

<p>The operating system keeps track of all lookaside lists that are currently in use. As both the amount of available nonpaged memory and the demand for lookaside list entries vary over time, the operating system dynamically adjusts its limits for the maximum number of entries in each nonpaged lookaside list.</p>

<p>In Windows 2000 and later versions of Windows, a lookaside list that contains paged or nonpaged entries can be described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff558775">PAGED_LOOKASIDE_LIST</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff556431">NPAGED_LOOKASIDE_LIST</a> structure, respectively.</p>

<p>For more information about lookaside lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

<p>Callers of <b>ExInitializeLookasideListEx</b> can be running at IRQL &lt;= DISPATCH_LEVEL, but are typically running at IRQL = PASSIVE_LEVEL.</p>

<p>The driver-supplied <i>LookasideListAllocateEx</i> and <i>LookasideListFreeEx</i> routines both receive <i>Lookaside</i> parameters that point to the <b>LOOKASIDE_LIST_EX</b> structure that describes the lookaside list. The routines can use this parameter to access private data that the driver has associated with the lookaside list. For example, the driver might allocate an instance of the following structure to collect private data for each lookaside list that it creates:</p>

<p>The driver can initialize a lookaside list as shown in the following code example:</p>

<p>The following code example shows how the <i>LookasideListAllocateEx</i> routine can use its <i>Lookaside</i> parameter to access the private data that is associated with the lookaside list:</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a> macro is defined in the Ntdef.h header file. The <i>LookAsideListFreeEx</i> routine can similarly use its <i>Lookaside</i> parameter to access private data.</p>

<p>After the <code>MyLookasideListAllocateEx</code> routine in this example returns, <b>ExAllocateFromLookasideListEx</b> inserts the buffer pointed to by the <code>NewEntry</code> variable into the lookaside list. To make this insertion operation thread-safe, <b>ExAllocateFromLookasideListEx</b> synchronizes its access of the lookaside list with other list insertion and removal operations that might be performed by other threads. Similarly, when <b>ExFreeFromLookasideListEx</b> removes a buffer from the lookaside list, it synchronizes its access to the list.</p>

<p><b>ExAllocateFromLookasideListEx</b> and <b>ExFreeFromLookasideListEx</b> do not synchronize their calls to driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554322">LookasideListAllocateEx</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554324">LookasideListFreeEx</a> routines. Thus, if the <code>MyLookasideListAllocateEx</code> and <code>MyLookasideListFreeEx</code> routines in the preceding code examples must be thread-safe, the driver must provide the necessary synchronization.</p>

<p>The example routine, <code>MyLookasideListAllocateEx</code>, synchronizes its access of the <code>MyContext-&gt;NumberOfAllocations</code> variable with other threads that might increment and decrement this variable. To provide this synchronization, <code>MyLookasideListAllocateEx</code> calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547910">InterlockedIncrement</a> routine to atomically increment this variable. Similarly, the <code>MyLookasideListFreeEx</code> routine (not shown) can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547871">InterlockedDecrement</a> routine to atomically decrement this variable.</p>

<p>However, if the sole purpose of the <code>MyContext-&gt;NumberOfAllocations</code> variable in the preceding code example is simply to gather statistics on lookaside list allocations, atomic increments and decrements are hardly necessary. In this case, the remote possibility of a missed increment or decrement should not be a concern.</p>

<p>For more information about thread safety for lookaside lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544381">ExAllocateFromLookasideListEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544513">ExAllocatePoolWithQuotaTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544563">ExDeleteLookasideListEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544597">ExFreeToLookasideListEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547871">InterlockedDecrement</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547910">InterlockedIncrement</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554322">LookasideListAllocateEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554324">LookasideListFreeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554329">LOOKASIDE_LIST_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556431">NPAGED_LOOKASIDE_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558775">PAGED_LOOKASIDE_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExInitializeLookasideListEx routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
