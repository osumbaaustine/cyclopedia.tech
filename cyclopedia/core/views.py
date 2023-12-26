import pandas as pd
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.utils.text import slugify
from django.views.generic import TemplateView, ListView

from .forms import ExcelUploadForm
from .models import Category, Subcategory, Entry


def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the Excel file using pandas
            excel_data = pd.read_excel(request.FILES['excel_file'])

            # Iterate through rows of the Excel sheet
            for index, row in excel_data.iterrows():
                # Create a dictionary to store field-value pairs
                entry_data = {}

                # Iterate through columns of the Excel sheet
                for col in excel_data.columns:
                    # Map Excel columns to Entry model fields (adjust as needed)
                    if col == 'Title':
                        entry_data['title'] = row[col]
                    elif col == 'url':
                        entry_data['url'] = row[col]
                    elif col == 'Description':
                        entry_data['description'] = row[col]
                    elif col == 'Author':
                        entry_data['author'] = row[col]
                    elif col == 'Owner':
                        entry_data['owner'] = row[col]
                    elif col == 'Category':
                        category, created = Category.objects.get_or_create(name=row[col])
                        entry_data['category'] = category
                    elif col == 'Subcategory':
                        subcategory, created = Subcategory.objects.get_or_create(name=row[col], category=category)
                        entry_data['subcategory'] = subcategory

                entry_data['slug'] = slugify(entry_data['title'])

                # Create an Entry object with the mapped data
                Entry.objects.create(**entry_data)

            return HttpResponse('Data from Excel uploaded successfully!')
    else:
        form = ExcelUploadForm()

    return render(request, 'core/upload_excel.html', {'form': form})


class Index(TemplateView):
    template_name = "core/index.html"


class AICategoryListView(ListView):
    model = Entry
    template_name = 'core/ai.html'
    context_object_name = 'ai_entries'

    def get_queryset(self):
        ai_category = Category.objects.get(name='AI')
        return Entry.objects.filter(category=ai_category).values()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ai_category'] = Category.objects.get(name='AI')
        context['ai_subcategories'] = Subcategory.objects.filter(category__name='AI')
        return context


def entry_detail(request, slug):
    template_name = "core/entry_detail.html"
    entry = get_object_or_404(Entry, slug=slug)

    return render(
        request,
        template_name,
        {
            "entry": entry,
        },
    )


class CryptoCategoryListView(ListView):
    model = Entry
    template_name = 'core/crypto.html'
    context_object_name = 'crypto_entries'

    # def get_queryset(self):
    #     crypto_category = Category.objects.get(name='Cryptocurrency')
    #     return Entry.objects.filter(category=crypto_category).values()
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['crypto_category'] = Category.objects.get(name='Cryptocurrency')
    #     context['crypto_subcategories'] = Subcategory.objects.filter(category__name='Cryptocurrency')
    #     return context

    # def get_queryset(self):
    #     crypto_category = Category.objects.get(name='Cryptocurrency')
    #     return Entry.objects.filter(category=crypto_category).values()
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['crypto_category'] = Category.objects.get(name='Cryptocurrency')
    #     return context
    # Assuming 'Cryptocurrency' is the category name you want to filter by
    def get_queryset(self):
        # Assuming 'Cryptocurrency' is the category name you want to filter by
        crypto_category = Category.objects.get(name='Cryptocurrency')
        subcategory_id = self.request.GET.get('subcategory')  # Get subcategory id from the query parameters

        if subcategory_id:
            # Filter entries by both category and subcategory
            return Entry.objects.filter(category=crypto_category, subcategory__id=subcategory_id).values()
        else:
            # If no subcategory selected, only filter by category
            return Entry.objects.filter(category=crypto_category).values()


class SAASCategoryListView(ListView):
    model = Entry
    template_name = 'core/saas.html'
    context_object_name = 'saas_entries'

    def get_queryset(self):
        saas_category = Category.objects.get(name='SAAS')
        return Entry.objects.filter(category=saas_category).values()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saas_category'] = Category.objects.get(name='SAAS')
        context['saas_subcategories'] = Subcategory.objects.filter(category__name='SAAS')
        return context


class BlockchainCategoryListView(ListView):
    model = Entry
    template_name = 'core/blockchain.html'
    context_object_name = 'blockchain_entries'

    def get_queryset(self):
        blockchain_category = Category.objects.get(name='Blockchain')
        return Entry.objects.filter(category=blockchain_category).values()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blockchain_category'] = Category.objects.get(name='Blockchain')
        context['blockchain_subcategories'] = Subcategory.objects.filter(category__name='Blockchain')
        return context

